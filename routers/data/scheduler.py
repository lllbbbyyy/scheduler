from tkinter import W
from .db_manage.models import Subject, Exam, ExamItem, LimitItem, Teacher, CourseItem, ScheduledItem
from .db_manage.database import get_db
from sqlalchemy.orm import Session
from .common_schema import TimeStr


def get_data_duty():
    db: Session = next(get_db())
    teacher_list: list[Teacher] = db.query(Teacher).filter(
        Teacher.need_duty == True).all()
    teacher_extra_info: dict[int, dict] = {}
    all_exam_hour = 0
    for teacher in teacher_list:
        teacher_extra_info[teacher.id] = {}
        #课程表信息
        teacher_extra_info[teacher.id]['course_item_list'] = db.query(
            CourseItem).filter(CourseItem.teacher_id == teacher.id).all()
        #已监考信息
        teacher_extra_info[teacher.id]['scheduled_item_type1_list'] = db.query(
            ScheduledItem).filter(ScheduledItem.teacher_id == teacher.id,
                                  ScheduledItem.type == 1).all()

        teacher_extra_info[teacher.id]['scheduled_item_type1_all_hour'] = 0
        for scheduled_item in teacher_extra_info[
                teacher.id]['scheduled_item_type1_list']:
            teacher_extra_info[
                teacher.id]['scheduled_item_type1_all_hour'] += TimeStr(
                    scheduled_item.end_time).sub_Timestr(
                        TimeStr(scheduled_item.begin_time))
        all_exam_hour += teacher_extra_info[
            teacher.id]['scheduled_item_type1_all_hour']

    teacher_list.sort(key=lambda x: teacher_extra_info[x.id][
        'scheduled_item_type1_all_hour'])
    return teacher_list, teacher_extra_info, all_exam_hour


def get_data(grade: str):
    db: Session = next(get_db())
    if grade == '高一':
        teacher_list: list[Teacher] = db.query(Teacher).filter(
            Teacher.grade1 == True).all()
    if grade == '高二':
        teacher_list: list[Teacher] = db.query(Teacher).filter(
            Teacher.grade2 == True).all()
    if grade == '高三':
        teacher_list: list[Teacher] = db.query(Teacher).filter(
            Teacher.grade3 == True).all()
    teacher_extra_info: dict[int, dict] = {}
    #统计所有教师的上课课时和监考时间
    all_class_times = 0
    all_exam_hour = 0
    for teacher in teacher_list:
        teacher_extra_info[teacher.id] = {}
        #课程表信息
        teacher_extra_info[teacher.id]['course_item_list'] = db.query(
            CourseItem).filter(CourseItem.teacher_id == teacher.id,
                               CourseItem.grade == grade).all()
        #已监考信息
        teacher_extra_info[teacher.id]['scheduled_item_list'] = db.query(
            ScheduledItem).filter(ScheduledItem.teacher_id == teacher.id,
                                  ScheduledItem.grade == grade,
                                  ScheduledItem.type == 0).all()

        teacher_extra_info[teacher.id]['course_item_list_len'] = len(
            teacher_extra_info[teacher.id]['course_item_list'])
        all_class_times += teacher_extra_info[
            teacher.id]['course_item_list_len'] + teacher.extra_hour

        teacher_extra_info[teacher.id]['scheduled_item_all_hour'] = 0
        for scheduled_item in teacher_extra_info[
                teacher.id]['scheduled_item_list']:
            teacher_extra_info[
                teacher.id]['scheduled_item_all_hour'] += TimeStr(
                    scheduled_item.end_time).sub_Timestr(
                        TimeStr(scheduled_item.begin_time))

        all_exam_hour += teacher_extra_info[
            teacher.id]['scheduled_item_all_hour']
        #按照监考时间占比系数+(课时数+班主任的额外时间)时间占比系数排序
    def get_teacher_list_key(x):
        r = 0
        if all_class_times != 0:
            r += (teacher_extra_info[x.id]['course_item_list_len'] +
                  x.extra_hour) / all_class_times
        if all_exam_hour != 0:
            r += teacher_extra_info[
                x.id]['scheduled_item_all_hour'] / all_exam_hour
        return r

    teacher_list.sort(key=get_teacher_list_key)
    return teacher_list, teacher_extra_info, all_class_times, all_exam_hour


def is_segment_has_interaction(t1_begin: str, t1_end: str, t1_week: int,
                               t2_begin: str, t2_end: str, t2_week: int):
    if t1_week != t2_week:
        return False
    if t1_end < t2_begin:
        return False
    if t2_end < t1_begin:
        return False
    return True


def scheduler(exam: Exam) -> bool:
    db: Session = next(get_db())
    exam_item_list: list[ExamItem] = db.query(ExamItem).filter(
        ExamItem.exam_id == exam.id, ExamItem.type == 0).all()
    #对待考试条目按照时间排序
    exam_item_list.sort(key=lambda x: str(x.week) + x.begin_time + x.end_time)
    for exam_item in exam_item_list:
        teacher_list, teacher_extra_info, _, _ = get_data(exam.grade)
        all_needed_num = exam_item.needed_num
        multi_exam_item_list: list[ExamItem] = []
        for _ in range(exam_item.needed_num):
            multi_exam_item_list.append(exam_item)
    # def get_key_for_teacher(teacher:Teacher):
    #     if Teacher.
        err_teacher_index = -1
        is_success = False
        needed_teacher_list = teacher_list[0:all_needed_num]
        for schedule_cnt in range(len(teacher_list) - all_needed_num):
            if schedule_cnt != 0 and err_teacher_index != -1:
                needed_teacher_list[err_teacher_index] = teacher_list[
                    all_needed_num + schedule_cnt]
                err_teacher_index = -1
            #构建邻接表，[0:all_needed_num)表示教师，[all_needed_num:2*all_needed_num)表示需要排考的科目
            g: list[list[int]] = []
            vis: list[int] = []
            match: list[int] = []
            for _ in range(2 * all_needed_num):
                g.append([])
                vis.append(0)
                match.append(-1)
            #建立邻接表
            for i in range(all_needed_num):
                teacher = needed_teacher_list[i]
                pre_exam_num = 0

                course_item_flag = False
                limit_item_flag = False
                for course_item in teacher_extra_info[
                        teacher.id]['course_item_list']:
                    if is_segment_has_interaction(
                            exam_item.begin_time, exam_item.end_time,
                            exam_item.week, course_item.begin_time,
                            course_item.end_time, course_item.week
                    ) and exam.grade != course_item.grade:
                        break
                else:
                    course_item_flag = True
                #对于限制条件进行排考
                limit_item_list = db.query(LimitItem).filter(
                    LimitItem.exam_id == exam.id,
                    LimitItem.teacher_id == teacher.id)
                for limit_item in limit_item_list:
                    if is_segment_has_interaction(exam_item.begin_time,
                                                  exam_item.end_time,
                                                  exam_item.week,
                                                  limit_item.begin_time,
                                                  limit_item.end_time,
                                                  limit_item.week):
                        break
                else:
                    limit_item_flag = True

                if course_item_flag and limit_item_flag:
                    #连边
                    for j in range(exam_item.needed_num):
                        g[i].append(all_needed_num + pre_exam_num + j)
                        g[all_needed_num + pre_exam_num + j].append(i)
                pre_exam_num += exam_item.needed_num
            #进行匈牙利算法
            match_num = 0

            def dfs(u: int) -> bool:
                for v in g[u]:
                    if vis[v]:
                        continue
                    vis[v] = 1
                    if match[v] == -1 or dfs(match[v]):
                        match[v] = u
                        match[u] = v
                        return True
                return False

            #从一侧的开始顶点到结束顶点
            for i in range(all_needed_num):
                for j in range(2 * all_needed_num):
                    vis[j] = 0
                if dfs(i):
                    match_num += 1
                else:
                    err_teacher_index = i
                    break
            #找到了一种匹配方法
            if match_num == all_needed_num:
                result: list[ScheduledItem] = []
                for i in range(all_needed_num):

                    result.append(
                        ScheduledItem(
                            teacher_id=teacher_list[i].id,
                            exam_id=exam.id,
                            begin_time=multi_exam_item_list[
                                match[i] - all_needed_num].begin_time,
                            end_time=multi_exam_item_list[
                                match[i] - all_needed_num].end_time,
                            week=multi_exam_item_list[match[i] -
                                                      all_needed_num].week,
                            grade=exam.grade))
                db.add_all(result)
                db.commit()
                is_success = True
                break
        if not is_success:
            db.query(ScheduledItem).filter(
                ScheduledItem.exam_id == exam.id).delete()
            db.commit()
            return False
    return True


def scheduler_for_duty(exam: Exam) -> bool:
    db: Session = next(get_db())
    exam_item_list: list[ExamItem] = db.query(ExamItem).filter(
        ExamItem.exam_id == exam.id, ExamItem.type == 1).all()
    #对待考试条目按照时间排序
    exam_item_list.sort(key=lambda x: str(x.week) + x.begin_time + x.end_time)
    for exam_item in exam_item_list:
        all_teacher_list, teacher_extra_info, _ = get_data_duty()
        teacher_list: list[Teacher] = []
        for teacher in all_teacher_list:
            if teacher.need_duty == True:
                teacher_list.append(teacher)
        teacher_list.sort(key=lambda x: teacher_extra_info[x.id][
            'scheduled_item_type1_all_hour'])
        all_needed_num = exam_item.needed_num
        multi_exam_item_list: list[ExamItem] = []
        for _ in range(exam_item.needed_num):
            multi_exam_item_list.append(exam_item)
    # def get_key_for_teacher(teacher:Teacher):
    #     if Teacher.
        err_teacher_index = -1
        is_success = False
        needed_teacher_list = teacher_list[0:all_needed_num]
        for schedule_cnt in range(len(teacher_list) - all_needed_num):
            if schedule_cnt != 0 and err_teacher_index != -1:
                needed_teacher_list[err_teacher_index] = teacher_list[
                    all_needed_num + schedule_cnt]
                err_teacher_index = -1
            #构建邻接表，[0:all_needed_num)表示教师，[all_needed_num:2*all_needed_num)表示需要排考的科目
            g: list[list[int]] = []
            vis: list[int] = []
            match: list[int] = []
            for _ in range(2 * all_needed_num):
                g.append([])
                vis.append(0)
                match.append(-1)
            #建立邻接表
            for i in range(all_needed_num):
                teacher = needed_teacher_list[i]
                pre_exam_num = 0

                course_item_flag = False
                limit_item_flag = False
                normal_item_flag=False
                for course_item in teacher_extra_info[
                        teacher.id]['course_item_list']:
                    if is_segment_has_interaction(
                            exam_item.begin_time, exam_item.end_time,
                            exam_item.week, course_item.begin_time,
                            course_item.end_time, course_item.week
                    ):
                        break
                else:
                    course_item_flag = True
                #对于限制条件进行排考
                limit_item_list = db.query(LimitItem).filter(
                    LimitItem.exam_id == exam.id,
                    LimitItem.teacher_id == teacher.id)
                for limit_item in limit_item_list:
                    if is_segment_has_interaction(exam_item.begin_time,
                                                  exam_item.end_time,
                                                  exam_item.week,
                                                  limit_item.begin_time,
                                                  limit_item.end_time,
                                                  limit_item.week):
                        break
                else:
                    limit_item_flag = True
                scheduled_item_list=db.query(ScheduledItem).filter(ScheduledItem.exam_id==exam.id,ScheduledItem.teacher_id==teacher.id,ScheduledItem.type==1).all()
                for scheduled_item in scheduled_item_list:
                    if is_segment_has_interaction(exam_item.begin_time,
                                                  exam_item.end_time,
                                                  exam_item.week,
                                                  scheduled_item.begin_time,
                                                  scheduled_item.end_time,
                                                  scheduled_item.week):
                        break
                else:
                    normal_item_flag=True
                if course_item_flag and limit_item_flag and normal_item_flag:
                    #连边
                    for j in range(exam_item.needed_num):
                        g[i].append(all_needed_num + pre_exam_num + j)
                        g[all_needed_num + pre_exam_num + j].append(i)
                pre_exam_num += exam_item.needed_num
            #进行匈牙利算法
            match_num = 0

            def dfs(u: int) -> bool:
                for v in g[u]:
                    if vis[v]:
                        continue
                    vis[v] = 1
                    if match[v] == -1 or dfs(match[v]):
                        match[v] = u
                        match[u] = v
                        return True
                return False

            #从一侧的开始顶点到结束顶点
            for i in range(all_needed_num):
                for j in range(2 * all_needed_num):
                    vis[j] = 0
                if dfs(i):
                    match_num += 1
                else:
                    err_teacher_index = i
                    break
            #找到了一种匹配方法
            if match_num == all_needed_num:
                result: list[ScheduledItem] = []
                for i in range(all_needed_num):

                    result.append(
                        ScheduledItem(
                            teacher_id=teacher_list[i].id,
                            exam_id=exam.id,
                            begin_time=multi_exam_item_list[
                                match[i] - all_needed_num].begin_time,
                            end_time=multi_exam_item_list[
                                match[i] - all_needed_num].end_time,
                            week=multi_exam_item_list[match[i] -
                                                      all_needed_num].week,
                            grade=exam.grade,
                            type=1))
                db.add_all(result)
                db.commit()
                is_success = True
                break
        if not is_success:
            db.query(ScheduledItem).filter(ScheduledItem.exam_id == exam.id,
                                           ScheduledItem.type == 1).delete()
            db.commit()
            return False
    return True


def scheduler_for_charge(exam: Exam) -> bool:
    db: Session = next(get_db())
    #这里0或者1都可以，1数据量小
    exam_item_list: list[ExamItem] = db.query(ExamItem).filter(
        ExamItem.exam_id == exam.id, ExamItem.type == 1).all()
    days_set = set()
    for exam_item in exam_item_list:
        days_set.add(exam_item.week)
    days_list: list[int] = list(days_set)
    days_list.sort()
    teacher_list = db.query(Teacher).filter(Teacher.need_charge == True).all()
    teacher_charge_cnt = {}
    for teacher in teacher_list:
        teacher_charge_cnt[teacher.id] = db.query(ScheduledItem).filter(
            ScheduledItem.type == 2,
            ScheduledItem.teacher_id == teacher.id).count()
    teacher_list.sort(key=lambda x: teacher_charge_cnt[x.id])
    scheduled_item_list = []
    teacher_list_len = len(teacher_list)
    for i in range(len(days_list)):
        scheduled_item_list.append(
            ScheduledItem(teacher_id=teacher_list[i % teacher_list_len].id,
                          exam_id=exam.id,
                          begin_time='00:00',
                          end_time='00:01',
                          week=days_list[i],
                          grade=exam.grade,
                          type=2))
    db.add_all(scheduled_item_list)
    db.commit()
    return True
