from fastapi.testclient import TestClient

import requests
from io import BytesIO

from requests_toolbelt import MultipartEncoder

import sys

sys.path.append('D:\\大四下\\毕业设计\\虚拟环境fastapi\\scheduler')

from scheduler.main import app

client = TestClient(app)


def test_exam_info_get():
    response = client.get('/data/exam_info?perPage=1&page=1')
    assert response.status_code == 200


def test_scheduled_items_get():
    response = client.get('/data/exam_info/scheduled_items?exam_id=1')
    assert response.status_code == 200


def test_scheduled_duty_items_get():
    response = client.get('/data/exam_info/scheduled_duty_items?exam_id=1')
    assert response.status_code == 200


def test_scheduled_charge_items_get():
    response = client.get('/data/exam_info/scheduled_charge_items?exam_id=1')
    assert response.status_code == 200


def test_all_excel_get():
    response = client.get('/data/exam_info/all_excel?exam_id=1')
    assert response.status_code == 200


def test_exam_info_put_delete():
    files = {
        'file':
        ('test.xlsx',
         open('D:\\大四下\\毕业设计\\虚拟环境fastapi\\scheduler\\test\\test_exam.xlsx',
              'rb'),
         'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    }
    response = client.put('/data/exam_info/file', files=files)
    assert response.status_code == 200
    assert response.json() == {"status": 0, "msg": "", "data": {}}
    response = client.delete('/data/exam_info', json={"exam_id": 2})
    assert response.status_code == 200
    assert response.json() == {"status": 0, "msg": "", "data": {}}


def test_exam_info_batch_delete():
    files = {
        'file':
        ('test.xlsx',
         open('D:\\大四下\\毕业设计\\虚拟环境fastapi\\scheduler\\test\\test_exam.xlsx',
              'rb'),
         'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    }
    response = client.put('/data/exam_info/file', files=files)
    assert response.status_code == 200
    assert response.json() == {"status": 0, "msg": "", "data": {}}
    response = client.delete('/data/exam_info/2')
    assert response.status_code == 200
    assert response.json() == {"status": 0, "msg": "", "data": {}}


def test_exam_info_post():
    files = {
        'file':
        ('test.xlsx',
         open('D:\\大四下\\毕业设计\\虚拟环境fastapi\\scheduler\\test\\test_exam.xlsx',
              'rb'),
         'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    }
    response = client.put('/data/exam_info/file', files=files)
    assert response.status_code == 200
    assert response.json() == {"status": 0, "msg": "", "data": {}}
    response = client.post('/data/exam_info/scheduled_items?exam_id=2',
                           json={
                               "rows": [{
                                   "time_segment": "08:00-09:30",
                                   "day4": "蔡宁",
                                   "day5": "武海勋"
                               }],
                               "rowsDiff": [{
                                   "time_segment": "08:00-09:30",
                                   "day4": "蔡宁"
                               }],
                               "indexes": ["0"],
                               "rowsOrigin": [{
                                   "time_segment": "08:00-09:30",
                                   "day4": "王正宇",
                                   "day5": "武海勋"
                               }],
                               "ids":
                               "08:00-09:30",
                               "unModifiedItems": [{
                                   "time_segment": "08:00-09:30",
                                   "day4": "鄂英姿",
                                   "day5": "俞颖婷"
                               }, {
                                   "time_segment": "08:00-09:30",
                                   "day4": "吉利",
                                   "day5": "祝芳"
                               }, {
                                   "time_segment": "08:00-09:30",
                                   "day4": "陈丽",
                                   "day5": "郭丽珍"
                               }, {
                                   "time_segment": "08:00-09:30",
                                   "day4": "蒋宁燕",
                                   "day5": "吉同林"
                               }, {
                                   "time_segment": "08:00-10:00",
                                   "day3": "武海勋"
                               }, {
                                   "time_segment": "08:00-10:00",
                                   "day3": "俞颖婷"
                               }, {
                                   "time_segment": "08:00-10:00",
                                   "day3": "祝芳"
                               }, {
                                   "time_segment": "08:00-10:00",
                                   "day3": "计忠发"
                               }, {
                                   "time_segment": "08:00-10:00",
                                   "day3": "严烨"
                               }, {
                                   "time_segment": "10:00-11:00",
                                   "day4": "郭丽珍",
                                   "day5": "王正宇"
                               }, {
                                   "time_segment": "10:00-11:00",
                                   "day4": "吉同林",
                                   "day5": "黄小媚"
                               }, {
                                   "time_segment": "10:00-11:00",
                                   "day4": "金欣欣",
                                   "day5": "林芷立"
                               }, {
                                   "time_segment": "10:00-11:00",
                                   "day4": "黄小媚",
                                   "day5": "应晓默"
                               }, {
                                   "time_segment": "10:00-11:00",
                                   "day4": "林芷立",
                                   "day5": "鄂英姿"
                               }, {
                                   "time_segment": "10:30-11:30",
                                   "day3": "王正宇"
                               }, {
                                   "time_segment": "10:30-11:30",
                                   "day3": "陈丽"
                               }, {
                                   "time_segment": "10:30-11:30",
                                   "day3": "蒋宁燕"
                               }, {
                                   "time_segment": "10:30-11:30",
                                   "day3": "金欣欣"
                               }, {
                                   "time_segment": "10:30-11:30",
                                   "day3": "徐兵兵"
                               }, {
                                   "time_segment": "13:00-14:00",
                                   "day3": "郭丽珍",
                                   "day4": "应晓默"
                               }, {
                                   "time_segment": "13:00-14:00",
                                   "day3": "吉同林",
                                   "day4": "凌一娜"
                               }, {
                                   "time_segment": "13:00-14:00",
                                   "day3": "黄小媚",
                                   "day4": "王霄"
                               }, {
                                   "time_segment": "13:00-14:00",
                                   "day3": "林芷立",
                                   "day4": "黄菁华"
                               }, {
                                   "time_segment": "13:00-14:00",
                                   "day3": "应晓默",
                                   "day4": "徐兵兵"
                               }]
                           })
    assert response.status_code == 200
    assert response.json() == {"status": 0, "msg": "", "data": {}}
    response = client.post('/data/exam_info/scheduled_duty_items?exam_id=2',
                           json={
                               "rows": [{
                                   "time_segment": "08:00-10:00",
                                   "day3": "蔡宁"
                               }],
                               "rowsDiff": [{
                                   "time_segment": "08:00-10:00",
                                   "day3": "蔡宁"
                               }],
                               "indexes": ["1"],
                               "rowsOrigin": [{
                                   "time_segment": "08:00-10:00",
                                   "day3": "严兆铭"
                               }],
                               "ids":
                               "08:00-10:00",
                               "unModifiedItems": [{
                                   "time_segment": "08:00-09:30",
                                   "day4": "葛畅",
                                   "day5": "汪伊娜"
                               }, {
                                   "time_segment": "10:00-11:00",
                                   "day4": "吉同林",
                                   "day5": "何宇澄"
                               }, {
                                   "time_segment": "10:30-11:30",
                                   "day3": "何宇澄"
                               }, {
                                   "time_segment": "13:00-14:00",
                                   "day3": "陈欣星",
                                   "day4": "皮艳婷"
                               }]
                           })
    assert response.status_code == 200
    assert response.json() == {"status": 0, "msg": "", "data": {}}
    response = client.post('/data/exam_info/scheduled_charge_items?exam_id=2',
                           json={
                               "rows": [{
                                   "day3": "吕宫",
                                   "day4": "时颖",
                                   "day5": "吕宫"
                               }],
                               "rowsDiff": [{
                                   "day3": "吕宫"
                               }],
                               "indexes": ["0"],
                               "rowsOrigin": [{
                                   "day3": "李鹏",
                                   "day4": "时颖",
                                   "day5": "吕宫"
                               }],
                               "unModifiedItems": []
                           })
    assert response.status_code == 200
    assert response.json() == {"status": 0, "msg": "", "data": {}}
    response = client.delete('/data/exam_info/2')
    assert response.status_code == 200
    assert response.json() == {"status": 0, "msg": "", "data": {}}
