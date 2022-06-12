from fastapi.testclient import TestClient

import requests
from io import BytesIO

from requests_toolbelt import MultipartEncoder

import sys

sys.path.append('D:\\大四下\\毕业设计\\虚拟环境fastapi\\scheduler')

from scheduler.main import app

client = TestClient(app)


def test_teacher_info_get():
    response = client.get('/data/teacher_info?perPage=6&page=1')
    assert response.status_code == 200
    assert response.json() == {
        "status": 0,
        "msg": "",
        "data": {
            "items": [{
                "teacher_name": "蔡宁",
                "extra_hour": 0
            }, {
                "teacher_name": "陈华",
                "extra_hour": 0
            }, {
                "teacher_name": "陈丽",
                "extra_hour": 0
            }, {
                "teacher_name": "陈欣星",
                "extra_hour": 0
            }, {
                "teacher_name": "陈盛",
                "extra_hour": 0
            }, {
                "teacher_name": "池鸿勤",
                "extra_hour": 0
            }],
            "total":
            75
        }
    }


def test_teacher_info_put_delete():
    response = client.put('/data/teacher_info',
                          json={
                              "extra_hour": "1",
                              "teacher_name": "测试",
                              "is_duty": True,
                              "is_charge": True
                          })
    assert response.status_code == 200
    assert response.json() == {"status": 0, "msg": "", "data": {}}
    response = client.delete('/data/teacher_info', json={"teacher_name": "测试"})
    assert response.status_code == 200
    assert response.json() == {"status": 0, "msg": "", "data": {}}


def test_teacher_info_batch_delete():
    response = client.put('/data/teacher_info',
                          json={
                              "extra_hour": "1",
                              "teacher_name": "测试",
                              "is_duty": True,
                              "is_charge": True
                          })
    assert response.status_code == 200
    assert response.json() == {"status": 0, "msg": "", "data": {}}
    response = client.delete('/data/teacher_info/测试')
    assert response.status_code == 200
    assert response.json() == {"status": 0, "msg": "", "data": {}}


def test_teacher_info_course_item_get():
    response = client.get('/data/teacher_info/course_items?teacher_name=蔡宁')
    assert response.status_code == 200
    assert response.json() == {
        "items": [{
            "day4": "高三2班\n体育\n高三1班\n体育",
            "day5": "高三4班\n体育\n高三3班\n体育",
            "time_segment": "09:00-09:40"
        }, {
            "day2": "高三4班\n体育\n高三3班\n体育",
            "day4": "高三3班\n体育专项\n高三4班\n体育专项",
            "day5": "高三2班\n体育专项\n高三1班\n体育专项",
            "time_segment": "10:10-10:50"
        }, {
            "day2": "高三1班\n体育\n高三2班\n体育",
            "day4": "高三4班\n体育专项\n高三3班\n体育专项",
            "day5": "高三2班\n体育专项\n高三1班\n体育专项",
            "time_segment": "11:05-11:45"
        }, {
            "day5": "高二1班\n体锻\n高二4班\n体锻\n高二3班\n体锻\n高二2班\n体锻",
            "time_segment": "13:00-13:40"
        }, {
            "day3": "高三4班\n体锻\n高三3班\n体锻\n高三2班\n体锻\n高三1班\n体锻",
            "time_segment": "14:45-15:25"
        }]
    }


def test_teacher_info_put():
    files = {
        'file':
        ('test.xlsx',
         open(
             'D:\\大四下\\毕业设计\\虚拟环境fastapi\\scheduler\\test\\test_put_teacher_info.xlsx',
             'rb'),
         'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    }
    response = client.put('/data/teacher_info/file', files=files)
    assert response.status_code == 200
    assert response.json() == {"status": 0, "msg": "", "data": {}}
    response = client.delete('/data/teacher_info', json={"teacher_name": "测试"})
    assert response.status_code == 200
    assert response.json() == {"status": 0, "msg": "", "data": {}}

def test_teacher_coursetable_put():
    response = client.put('/data/teacher_info',
                          json={
                              "extra_hour": "1",
                              "teacher_name": "测试",
                              "is_duty": True,
                              "is_charge": True
                          })
    assert response.status_code == 200
    assert response.json() == {"status": 0, "msg": "", "data": {}}
    files = {
        'file':
        ('test.xlsx',
         open(
             'D:\\大四下\\毕业设计\\虚拟环境fastapi\\scheduler\\test\\test_teacher_coursetable.xlsx',
             'rb'),
         'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    }
    response = client.put('/data/teacher_coursetable_info/file', files=files)
    assert response.status_code == 200
    assert response.json() == {"status": 0, "msg": "", "data": {}}
    response = client.delete('/data/teacher_info', json={"teacher_name": "测试"})
    assert response.status_code == 200
    assert response.json() == {"status": 0, "msg": "", "data": {}}