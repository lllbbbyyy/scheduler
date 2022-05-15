from fastapi import APIRouter, Path, Depends, UploadFile
from typing import Optional
from pydantic import BaseModel
from sqlalchemy.orm import Session
from tempfile import NamedTemporaryFile
from .common_schema import Result
from .db_manage.models import ScheduledItem, Teacher, CourseItem, ExamItem, LimitItem
from .db_manage.database import get_db

import openpyxl


class Item(BaseModel):
    teacher_name: str


router = APIRouter()


@router.get("/teacher_info/course_items", description='查询教师课表信息')
async def get_all_item(teacher_name: str, db: Session = Depends(get_db)):
    t: Teacher = db.query(Teacher).filter(Teacher.name == teacher_name).first()
    course_items_list: list[CourseItem] = db.query(CourseItem).filter(
        CourseItem.teacher_id == t.id).all()
    course_items_dict = {}
    for course_item in course_items_list:
        time_segment = course_item.begin_time + '-' + course_item.end_time
        if time_segment not in course_items_dict.keys():
            course_items_dict[time_segment] = {}
        course_items_dict[time_segment][
            'day' + str(course_item.week)] = course_item.content
    sorted_items = sorted(course_items_dict.items(), key=lambda x: x[0])
    r_data = {'items': []}
    for sorted_item in sorted_items:
        r_data['items'].append(sorted_item[1])
        r_data['items'][-1]['time_segment'] = sorted_item[0]
    return r_data


@router.get("/teacher_info", description='查询所有教师信息（不包括贡献度）')
async def get_all_item(page: Optional[int] = None,
                       perPage: Optional[int] = None,
                       db: Session = Depends(get_db)):
    all_item: list[Teacher] = db.query(Teacher).all()
    items_list = {'items': []}
    for item in all_item:
        items_list["items"].append(Item(teacher_name=item.name))
    r = Result(data=items_list)
    return r


@router.delete("/teacher_info/{teacher_name}", description='批量删除数据')
async def batch_delete(teacher_name: str = Path(..., title='通过,分隔'),
                       db: Session = Depends(get_db)):
    teacher_name_list = teacher_name.split(',')
    for teacher_name in teacher_name_list:
        teacher = db.query(Teacher).filter(
            Teacher.name == teacher_name).first()
        db.query(CourseItem).filter(
            CourseItem.teacher_id == teacher.id).delete()
        o = db.query(LimitItem).filter(
            LimitItem.teacher_id == teacher.id).first()
        if o is not None:
            return Result(status=-1,
                          msg='请先删除包含教师：' + teacher_name + '的考试后再删除该教师')
        o = db.query(ScheduledItem).filter(
            ScheduledItem.teacher_id == teacher.id).first()
        if o is not None:
            return Result(status=-1,
                          msg='请先删除包含教师：' + teacher_name + '的考试后再删除该教师')
        db.query(Teacher).filter(Teacher.name == teacher_name).delete()
    db.commit()
    return Result()


@router.delete("/teacher_info", description='单个删除数据')
async def item_delete(item: Item, db: Session = Depends(get_db)):
    teacher = db.query(Teacher).filter(
        Teacher.name == item.teacher_name).first()
    db.query(CourseItem).filter(CourseItem.teacher_id == teacher.id).delete()
    o = db.query(LimitItem).filter(LimitItem.teacher_id == teacher.id).first()
    if o is not None:
        return Result(status=-1, msg='请先删除包含教师：' + teacher.name + '的考试后再删除该教师')
    o = db.query(ScheduledItem).filter(
        ScheduledItem.teacher_id == teacher.id).first()
    if o is not None:
        return Result(status=-1, msg='请先删除包含教师：' + teacher.name + '的考试后再删除该教师')
    db.query(Teacher).filter(Teacher.name == item.teacher_name).delete()
    db.commit()
    return Result()


@router.put("/teacher_info", description='增添教师信息')
async def add_item(item: Item, db: Session = Depends(get_db)):
    db_item = Teacher(name=item.teacher_name)
    if db.query(Teacher).filter(Teacher.name == db_item.name).first():
        return Result(status=-1, msg='已有该教师')
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return Result()


@router.put("/teacher_info/file", description='通过文件增添教师信息')
async def add_item(file: UploadFile, db: Session = Depends(get_db)):
    contents = await file.read()
    with NamedTemporaryFile(mode='rb+', suffix='.xlsx') as tmp:
        tmp.write(contents)
        tmp.seek(0)
        wb = openpyxl.load_workbook(tmp)
    db_item_list = []
    for ws in wb:
        for row in ws.iter_rows():
            for cell in row:
                v: str = cell.value
                if isinstance(v, str) and v[0] != '#':
                    db_item = Teacher(name=v)
                    if db.query(Teacher).filter(
                            Teacher.name == db_item.name).first():
                        return Result(status=-1,
                                      msg=ws.title + '表第' + str(cell.row) +
                                      '行，第' + str(cell.column) + '列：' + v +
                                      '，已有该教师，导入失败')
                    db_item_list.append(db_item)
    db.add_all(db_item_list)
    db.commit()
    return Result()