from tkinter import W
from .db_manage.models import Subject, Exam, ExamItem, LimitItem, Teacher, CourseItem, ScheduledItem
from .db_manage.database import get_db
from sqlalchemy.orm import Session
from .common_schema import TimeStr


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
                                  ScheduledItem.grade == grade).all()
        teacher_extra_info[teacher.id]['course_item_list_len'] = len(
            teacher_extra_info[teacher.id]['course_item_list'])
        all_class_times += teacher_extra_info[
            teacher.id]['course_item_list_len'] + teacher.extra_hour
        teacher_extra_info[teacher.id]['scheduled_item_list_len'] = len(
            teacher_extra_info[teacher.id]['scheduled_item_list'])
        all_exam_hour += teacher_extra_info[
            teacher.id]['scheduled_item_list_len']
        #按照监考时间占比系数+(课时数+班主任的额外时间)时间占比系数排序
    def get_teacher_list_key(x):
        r = 0
        if all_class_times != 0:
            r += (teacher_extra_info[x.id]['course_item_list_len'] +
                  x.extra_hour) / all_class_times
        if all_exam_hour != 0:
            r += teacher_extra_info[
                x.id]['scheduled_item_list_len'] / all_exam_hour
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
    teacher_list, teacher_extra_info, all_class_times, all_exam_hour = get_data(
        exam.grade)

    db: Session = next(get_db())
    exam_item_list: list[ExamItem] = db.query(ExamItem).filter(
        ExamItem.exam_id == exam.id).all()
    all_needed_num = 0
    #对待考试条目按照时间排序
    exam_item_list.sort(key=lambda x: str(x.week) + x.begin_time + x.end_time)
    # teacher_sort_key:dict[str:int]={}
    # w=len(exam_item_list)
    # for exam_item in exam_item_list:
    #     teacher_extra_info[db.query(Subject).filter(Subject.id==exam_item.subject_id).first().name]=W
    #     w-=1
    #统计需要多少老师参与监考
    multi_exam_item_list: list[ExamItem] = []
    for exam_item in exam_item_list:
        all_needed_num += exam_item.needed_num
        for _ in range(exam_item.needed_num):
            multi_exam_item_list.append(exam_item)
    # def get_key_for_teacher(teacher:Teacher):
    #     if Teacher.
    begin_index = 0
    while begin_index + all_needed_num <= len(teacher_list):
        needed_teacher_list = teacher_list[begin_index:begin_index +
                                           all_needed_num]
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
            for exam_item in exam_item_list:
                for course_item in teacher_extra_info[
                        teacher.id]['course_item_list']:
                    if is_segment_has_interaction(exam_item.begin_time,
                                                  exam_item.end_time,
                                                  exam_item.week,
                                                  course_item.begin_time,
                                                  course_item.end_time,
                                                  course_item.week) and exam.grade!=course_item.grade:
                        break
                else:
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
                        end_time=multi_exam_item_list[match[i] -
                                                      all_needed_num].end_time,
                        week=multi_exam_item_list[match[i] -
                                                  all_needed_num].week,
                        grade=exam.grade))
            db.add_all(result)
            db.commit()
            return True
        begin_index += 1
    return False
