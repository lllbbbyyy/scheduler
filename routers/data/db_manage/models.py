from calendar import week
from datetime import datetime
from enum import unique
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime

from .database import Base


class Subject(Base):
    __tablename__ = 'subject'

    id = Column(Integer,
                primary_key=True,
                index=True,
                unique=True,
                autoincrement=True,
                nullable=False)
    name = Column(String(20), index=True, unique=True, nullable=False)


class Teacher(Base):
    __tablename__ = 'teacher'
    id = Column(Integer,
                primary_key=True,
                index=True,
                unique=True,
                autoincrement=True,
                nullable=False)
    name = Column(String(20), index=True, unique=True, nullable=False)
    #contribution = Column(Float, default=0, server_default='0')
    extra_hour = Column(Float, default=0, server_default='0')
    grade1 = Column(Boolean, default=False, server_default='False')
    grade2 = Column(Boolean, default=False, server_default='False')
    grade3 = Column(Boolean, default=False, server_default='False')
    #执勤
    need_duty = Column(Boolean, default=False, server_default='False')
    #主考
    need_charge = Column(Boolean, default=False, server_default='False')


class CourseItem(Base):
    __tablename__ = 'course_item'
    id = Column(Integer,
                primary_key=True,
                index=True,
                unique=True,
                autoincrement=True,
                nullable=False)
    teacher_id = Column(Integer, ForeignKey('teacher.id'), nullable=False)
    begin_time = Column(String(20), nullable=False)
    end_time = Column(String(20), nullable=False)
    week = Column(Integer, nullable=False)
    grade = Column(String(5), nullable=False)
    content = Column(String(50))


class Exam(Base):
    __tablename__ = 'exam'
    id = Column(Integer,
                primary_key=True,
                index=True,
                unique=True,
                autoincrement=True,
                nullable=False)
    name = Column(String(50))
    create_time = Column(DateTime)
    grade = Column(String(5), nullable=False)


#考试需满足的要求
class ExamItem(Base):
    __tablename__ = 'exam_item'
    id = Column(Integer,
                primary_key=True,
                index=True,
                unique=True,
                autoincrement=True,
                nullable=False)
    subject_id = Column(Integer, ForeignKey('subject.id'), nullable=False)
    exam_id = Column(Integer, ForeignKey('exam.id'), nullable=False)
    needed_num = Column(Integer, nullable=False)
    begin_time = Column(String(20), nullable=False)
    end_time = Column(String(20), nullable=False)
    week = Column(Integer, nullable=False)
    #0表示正常考试，1表示两处需求
    type = Column(Integer, default=0, server_default='0')

    def clone(self):
        return ExamItem(subject_id=self.subject_id,
                        exam_id=self.exam_id,
                        needed_num=self.needed_num,
                        begin_time=self.begin_time,
                        end_time=self.end_time,
                        week=self.week,
                        type=self.type)


class LimitItem(Base):
    __tablename__ = 'limit_item'
    id = Column(Integer,
                primary_key=True,
                index=True,
                unique=True,
                autoincrement=True,
                nullable=False)
    teacher_id = Column(Integer, ForeignKey('teacher.id'), nullable=False)
    exam_id = Column(Integer, ForeignKey('exam.id'), nullable=False)
    begin_time = Column(String(20), nullable=False)
    end_time = Column(String(20), nullable=False)
    week = Column(Integer, nullable=False)


#已排考试条目信息
class ScheduledItem(Base):
    __tablename__ = 'scheduled_item'
    id = Column(Integer,
                primary_key=True,
                index=True,
                unique=True,
                autoincrement=True,
                nullable=False)
    teacher_id = Column(Integer, ForeignKey('teacher.id'), nullable=False)
    exam_id = Column(Integer, ForeignKey('exam.id'), nullable=False)
    begin_time = Column(String(20), nullable=False)
    end_time = Column(String(20), nullable=False)
    week = Column(Integer, nullable=False)
    grade = Column(String(5), nullable=False)
    #0表示正常条目，1表示两处需求，2表示行政需求
    type = Column(Integer, default=0, server_default='0')
