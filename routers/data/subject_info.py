from ast import Sub
from fastapi import APIRouter, Path, Depends
from typing import Optional
from pydantic import BaseModel
from sqlalchemy.orm import Session
from .common_schema import Result
from .db_manage.models import Subject
from .db_manage.database import get_db


class Item(BaseModel):
    subject_name: str


router = APIRouter()


@router.get("/subject_info", description='查询所有科目信息')
async def get_all_item(page: Optional[int] = None,
                       perPage: Optional[int] = None,
                       db: Session = Depends(get_db)):
    all_item = db.query(Subject).all()
    items_list = {'items': []}
    for item in all_item:
        items_list["items"].append(Item(subject_name=item.name))
    r = Result(data=items_list)
    return r


@router.delete("/subject_info/{subject_name}", description='批量删除数据')
async def batch_delete(subject_name: str = Path(..., title='通过,分隔'),
                       db: Session = Depends(get_db)):
    subject_name_list = subject_name.split(',')
    for subject_name in subject_name_list:
        db.query(Subject).filter(Subject.name == subject_name).delete()
    db.commit()
    return Result()


@router.delete("/subject_info", description='单个删除数据')
async def item_delete(item: Item, db: Session = Depends(get_db)):
    db.query(Subject).filter(Subject.name == item.subject_name).delete()
    db.commit()
    return Result()


@router.post("/subject_info", description='增添科目信息')
async def add_item(item: Item, db: Session = Depends(get_db)):
    db_item = Subject(name=item.subject_name)
    if db.query(Subject).filter(Subject.name == db_item.name).first():
        return Result(status=-1, msg='已有该科目')
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return Result()