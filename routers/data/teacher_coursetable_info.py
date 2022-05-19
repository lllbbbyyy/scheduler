from fastapi import APIRouter, Path, Depends, UploadFile
from typing import Optional
from pydantic import BaseModel
from tempfile import NamedTemporaryFile
from sqlalchemy import false
from sqlalchemy.orm import Session
from .common_schema import Result, TimeStr
from .db_manage.models import Teacher, CourseItem
from .db_manage.database import get_db

import openpyxl
import re

# class Item(BaseModel):
#     teacher_name: str

router = APIRouter()

# @router.get("/teacher_info", description='查询所有教师信息（不包括贡献度）')
# async def get_all_item(page: Optional[int] = None,
#                        perPage: Optional[int] = None,
#                        db: Session = Depends(get_db)):
#     all_item: list[Teacher] = db.query(Teacher).all()
#     items_list = {'items': []}
#     for item in all_item:
#         items_list["items"].append(Item(teacher_name=item.name))
#     r = Result(data=items_list)
#     return r

# @router.delete("/teacher_info/{teacher_name}", description='批量删除数据')
# async def batch_delete(teacher_name: str = Path(..., title='通过,分隔'),
#                        db: Session = Depends(get_db)):
#     teacher_name_list = teacher_name.split(',')
#     for teacher_name in teacher_name_list:
#         db.query(Teacher).filter(Teacher.name == teacher_name).delete()
#     db.commit()
#     return Result()

# @router.delete("/teacher_info", description='单个删除数据')
# async def item_delete(item: Item, db: Session = Depends(get_db)):
#     db.query(Teacher).filter(Teacher.name == item.teacher_name).delete()
#     db.commit()
#     return Result()


@router.put("/teacher_coursetable_info/file", description='通过文件增添教师课表信息')
async def add_coursetable(file: UploadFile, db: Session = Depends(get_db)):
    contents = await file.read()
    with NamedTemporaryFile(mode='rb+', suffix='.xlsx') as tmp:
        tmp.write(contents)
        tmp.seek(0)
        wb = openpyxl.load_workbook(tmp)
    course_item_list = []
    teacher_grade_dict: dict[str, dict] = {}
    for ws in wb:
        teacher_name = ''
        for row in ws.iter_rows():
            time_seg = None
            cnt = 0
            for cell in row:
                v: str = cell.value
                #清洗数据
                if isinstance(v, str):
                    v = v.replace('_x000D_', '')
                #获取教师名称，以便后续存储年级信息
                if isinstance(v, str) and '教师：' in v:
                    teacher_name = v.split('：')[-1]
                    teacher_grade_dict[teacher_name] = {
                        'grade1': 0,
                        'grade2': 0,
                        'grade3': 0
                    }
                    teacher_item = db.query(Teacher).filter(
                        Teacher.name == teacher_name).first()
                    if teacher_item is None:
                        return Result(status=-1,
                                      msg='数据库中不存在教师：' + teacher_name)
                    db.query(CourseItem).filter(
                        CourseItem.teacher_id == teacher_item.id).delete()
                if isinstance(v, str) and '教师:' in v:
                    teacher_name = v.split(':')[-1]
                    teacher_grade_dict[teacher_name] = {
                        'grade1': 0,
                        'grade2': 0,
                        'grade3': 0
                    }
                    teacher_item = db.query(Teacher).filter(
                        Teacher.name == teacher_name).first()
                    if teacher_item is None:
                        return Result(status=-1,
                                      msg='数据库中不存在教师：' + teacher_name)
                    db.query(CourseItem).filter(
                        CourseItem.teacher_id == teacher_item.id).delete()
                if time_seg:
                    cnt += 1
                if v and cnt >= 1 and cnt <= 7 and teacher_name:
                    if not (isinstance(v, str) and v[0] == '#'):
                        course_item = CourseItem(teacher_id=teacher_item.id,
                                                 begin_time=time_seg[0],
                                                 end_time=time_seg[1],
                                                 week=cnt,
                                                 content=str(v),
                                                 grade='')
                    if isinstance(v, str):
                        if '高一' in v:
                            teacher_grade_dict[teacher_name]['grade1'] += 1
                            course_item.grade = '高一'
                        if '高二' in v:
                            teacher_grade_dict[teacher_name]['grade2'] += 1
                            course_item.grade = '高二'
                        if '高三' in v:
                            teacher_grade_dict[teacher_name]['grade3'] += 1
                            course_item.grade = '高三'

                    course_item_list.append(course_item)
                if isinstance(v, str):
                    re_res = re.search(r'(\d{1,2}:\d{2})-(\d{1,2}:\d{2})', v)
                if re_res:
                    time_seg: list[str] = list(re_res.groups())
                    time_seg[0] = str(TimeStr(time_seg[0]))
                    time_seg[1] = str(TimeStr(time_seg[1]))
                    #print(time_seg)
    db.add_all(course_item_list)
    db.commit()
    if len(teacher_grade_dict) != 0:
        for k, v in teacher_grade_dict.items():
            max_vv = 0
            for _, vv in v.items():
                max_vv = max(max_vv, vv)
            if max_vv==0:
                break
            update_data = {}
            for kk, vv in v.items():
                update_data[kk] = False
            for kk, vv in v.items():
                if vv == max_vv:
                    update_data[kk] = True
                    db.query(Teacher).filter(Teacher.name == k).update(
                        update_data, synchronize_session="fetch")
                    break
        db.commit()
    # db_item = Teacher(name=item.teacher_name)
    # if db.query(Teacher).filter(Teacher.name == db_item.name).first():
    #     return Result(status=-1, msg='已有该教师')
    # db.add(db_item)
    # db.commit()
    # db.refresh(db_item)
    return Result()
