from audioop import reverse
from fastapi import APIRouter, Path, Depends, UploadFile
from tempfile import NamedTemporaryFile
from typing import Optional
from pydantic import BaseModel
from sqlalchemy.orm import Session
from .common_schema import Result, TimeStr
from .db_manage.models import Subject, Exam, ExamItem, LimitItem, Teacher, ScheduledItem
from .db_manage.database import get_db
from .scheduler import get_data_duty, scheduler, get_data

import datetime
import openpyxl


class Item(BaseModel):
    teacher_name: str
    class_contribution: float
    exam_contribution: float
    all_contribution: float
    extra_class_num: float
    week_class_num: float
    exam_hour_sum: float


router = APIRouter()


@router.get("/statistics/class_hour_charts", description='获取课时图表信息')
async def get_class_hour_charts(grade: str):
    teacher_list, teacher_extra_info, all_class_times, all_exam_hour = get_data(
        grade)
    teacher_list.sort(key=lambda x: teacher_extra_info[x.id][
        'course_item_list_len'] + x.extra_hour)
    teacher_list.reverse()
    data = {
        'title': {},
        'tooltip': {},
        'legend': {},
        'xAxis': {
            'axisLabel': {
                'interval': 0
            }
        },
        'yAxis': {},
        'series': []
    }
    data['title']['text'] = '课时统计表'
    data['legend']['data'] = ['总课时数（包含班主任额外课时）']
    data['xAxis']['data'] = []
    data['series'] = [{"name": '总课时数（包含班主任额外课时）', 'type': 'bar', 'data': []}]
    for teacher in teacher_list:
        data['xAxis']['data'].append(teacher.name)
        data['series'][0]['data'].append(
            teacher_extra_info[teacher.id]['course_item_list_len'] +
            teacher.extra_hour)

    return Result(data=data)


@router.get("/statistics/exam_hour_charts", description='获取监考时间图表信息')
async def get_class_hour_charts(grade: str):
    teacher_list, teacher_extra_info, all_class_times, all_exam_hour = get_data(
        grade)
    teacher_list.sort(
        key=lambda x: teacher_extra_info[x.id]['scheduled_item_all_hour'])
    teacher_list.reverse()
    data = {
        'title': {},
        'tooltip': {},
        'legend': {},
        'xAxis': {
            'axisLabel': {
                'interval': 0
            }
        },
        'yAxis': {},
        'series': []
    }
    data['title']['text'] = '监考时间统计表'
    data['legend']['data'] = ['总监考时长']
    data['xAxis']['data'] = []
    data['series'] = [{"name": '总监考时长', 'type': 'bar', 'data': []}]
    for teacher in teacher_list:
        data['xAxis']['data'].append(teacher.name)
        data['series'][0]['data'].append(
            teacher_extra_info[teacher.id]['scheduled_item_all_hour'])

    return Result(data=data)


@router.get("/statistics/all_contribution_charts", description='获取总贡献度信息')
async def get_class_hour_charts(grade: str):
    teacher_list, teacher_extra_info, all_class_times, all_exam_hour = get_data(
        grade)
    teacher_list.reverse()
    data = {
        'title': {},
        'tooltip': {},
        'legend': {},
        'xAxis': {
            'axisLabel': {
                'interval': 0
            }
        },
        'yAxis': {},
        'series': []
    }
    data['title']['text'] = '总贡献度统计表'
    data['legend']['data'] = ['贡献系数和']
    data['xAxis']['data'] = []
    data['series'] = [{"name": '贡献系数和', 'type': 'bar', 'data': []}]
    for teacher in teacher_list:
        data['xAxis']['data'].append(teacher.name)
        if all_class_times == 0:
            class_contribution = 0
        else:
            class_contribution = (
                teacher_extra_info[teacher.id]['course_item_list_len'] +
                teacher.extra_hour) / all_class_times
        if all_exam_hour == 0:
            exam_contribution = 0
        else:
            exam_contribution = teacher_extra_info[
                teacher.id]['scheduled_item_all_hour'] / all_exam_hour
        data['series'][0]['data'].append(class_contribution +
                                         exam_contribution)

    return Result(data=data)


@router.get("/statistics/duty_hour_charts", description='获取统计信息')
async def get_charts():
    teacher_list, teacher_extra_info, all_exam_hour = get_data_duty()
    teacher_list.reverse()
    data = {
        'title': {},
        'tooltip': {},
        'legend': {},
        'xAxis': {
            'axisLabel': {
                'interval': 0
            }
        },
        'yAxis': {},
        'series': []
    }
    data['title']['text'] = '两处贡献度统计表'
    data['legend']['data'] = ['两处监考时长']
    data['xAxis']['data'] = []
    data['series'] = [{"name": '两处监考时长', 'type': 'bar', 'data': []}]
    for teacher in teacher_list:
        data['xAxis']['data'].append(teacher.name)
        data['series'][0]['data'].append(teacher_extra_info[teacher.id]['scheduled_item_type1_all_hour'])

    return Result(data=data)


@router.get("/statistics/duty", description='获取统计信息')
async def get_statistics(page: Optional[int] = None,
                         perPage: Optional[int] = None,
                         db: Session = Depends(get_db)):
    teacher_list, teacher_extra_info, all_exam_hour = get_data_duty()
    teacher_list.reverse()
    item_list: list[dict] = []
    for teacher in teacher_list:
        item_list.append({
            'teacher_name':
            teacher.name,
            'exam_hour':
            teacher_extra_info[teacher.id]['scheduled_item_type1_all_hour']
        })
    data = {
        'items': item_list,
    }
    r = Result(data=data)
    return r

@router.get("/statistics/charge_hour_charts", description='获取统计信息')
async def get_charts():
    db=next(get_db())
    teacher_list = db.query(Teacher).filter(Teacher.need_charge == True).all()
    teacher_charge_cnt = {}
    for teacher in teacher_list:
        teacher_charge_cnt[teacher.id] = db.query(ScheduledItem).filter(
            ScheduledItem.type == 2,
            ScheduledItem.teacher_id == teacher.id).count()
    teacher_list.sort(key=lambda x: teacher_charge_cnt[x.id])
    teacher_list.reverse()
    data = {
        'title': {},
        'tooltip': {},
        'legend': {},
        'xAxis': {
            'axisLabel': {
                'interval': 0
            }
        },
        'yAxis': {},
        'series': []
    }
    data['title']['text'] = '行政贡献度统计表'
    data['legend']['data'] = ['行政监考次数']
    data['xAxis']['data'] = []
    data['series'] = [{"name": '行政监考次数', 'type': 'bar', 'data': []}]
    for teacher in teacher_list:
        data['xAxis']['data'].append(teacher.name)
        data['series'][0]['data'].append(teacher_charge_cnt[teacher.id])

    return Result(data=data)


@router.get("/statistics/charge", description='获取统计信息')
async def get_statistics(page: Optional[int] = None,
                         perPage: Optional[int] = None,
                         db: Session = Depends(get_db)):
    teacher_list = db.query(Teacher).filter(Teacher.need_charge == True).all()
    teacher_charge_cnt = {}
    for teacher in teacher_list:
        teacher_charge_cnt[teacher.id] = db.query(ScheduledItem).filter(
            ScheduledItem.type == 2,
            ScheduledItem.teacher_id == teacher.id).count()
    teacher_list.sort(key=lambda x: teacher_charge_cnt[x.id])
    teacher_list.reverse()
    item_list: list[dict] = []
    for teacher in teacher_list:
        item_list.append({
            'teacher_name':
            teacher.name,
            'exam_hour':
            teacher_charge_cnt[teacher.id]
        })
    data = {
        'items': item_list,
    }
    r = Result(data=data)
    return r



@router.get("/statistics", description='获取统计信息')
async def get_statistics(grade: str,
                         page: Optional[int] = None,
                         perPage: Optional[int] = None,
                         db: Session = Depends(get_db)):
    teacher_list, teacher_extra_info, all_class_times, all_exam_hour = get_data(
        grade)
    teacher_list.reverse()
    item_list: list[Item] = []
    for teacher in teacher_list:
        if all_class_times == 0:
            class_contribution = 0
        else:
            class_contribution = (
                teacher_extra_info[teacher.id]['course_item_list_len'] +
                teacher.extra_hour) / all_class_times
        if all_exam_hour == 0:
            exam_contribution = 0
        else:
            exam_contribution = teacher_extra_info[
                teacher.id]['scheduled_item_all_hour'] / all_exam_hour
        item_list.append(
            Item(teacher_name=teacher.name,
                 class_contribution=class_contribution,
                 exam_contribution=exam_contribution,
                 all_contribution=exam_contribution + class_contribution,
                 extra_class_num=teacher.extra_hour,
                 week_class_num=teacher_extra_info[
                     teacher.id]['course_item_list_len'],
                 exam_hour_sum=teacher_extra_info[teacher.id]
                 ['scheduled_item_all_hour']))
    data = {
        'items': item_list,
        'exam_all_num': db.query(Exam).filter(Exam.grade == grade).count(),
        'exam_all_hour': all_exam_hour,
        'exam_all_teacher': len(teacher_list),
        'exam_arr_num': 0,
        'exam_arr_hour': 0
    }
    if len(teacher_list) != 0:
        data['exam_arr_hour'] = all_exam_hour / data['exam_all_teacher']
        data['exam_arr_num'] = data['exam_all_num'] / data['exam_all_teacher']

    r = Result(data=data)
    return r


# @router.delete("/subject_info/{subject_name}", description='批量删除数据')
# async def batch_delete(subject_name: str = Path(..., title='通过,分隔'),
#                        db: Session = Depends(get_db)):
#     subject_name_list = subject_name.split(',')
#     for subject_name in subject_name_list:
#         db.query(Subject).filter(Subject.name == subject_name).delete()
#     db.commit()
#     return Result()

# @router.delete("/subject_info", description='单个删除数据')
# async def item_delete(item: Item, db: Session = Depends(get_db)):
#     db.query(Subject).filter(Subject.name == item.subject_name).delete()
#     db.commit()
#     return Result()

# @router.put("/subject_info", description='增添科目信息')
# async def add_item(item: Item, db: Session = Depends(get_db)):
#     db_item = Subject(name=item.subject_name)
#     if db.query(Subject).filter(Subject.name == db_item.name).first():
#         return Result(status=-1, msg='已有该科目')
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return Result()