from fastapi.testclient import TestClient

import sys

sys.path.append('D:\\大四下\\毕业设计\\虚拟环境fastapi\\scheduler')

from scheduler.main import app

client = TestClient(app)


def test_page_index():
    response = client.get('/page/index')
    assert response.status_code == 200


def test_page_subject_info():
    response = client.get('/page/subject_info')
    assert response.status_code == 200


def test_page_teacher_info():
    response = client.get('/page/teacher_info')
    assert response.status_code == 200


def test_page_exam_info():
    response = client.get('/page/exam_info')
    assert response.status_code == 200


def test_page_statistics():
    response = client.get('/page/statistics?grade=高一')
    assert response.status_code == 200
    response = client.get('/page/statistics?grade=高二')
    assert response.status_code == 200
    response = client.get('/page/statistics?grade=高三')
    assert response.status_code == 200


def test_page_statistics_select():
    response = client.get('/page/statistics_select')
    assert response.status_code == 200


def test_page_statistics_duty():
    response = client.get('/page/statistics/duty')
    assert response.status_code == 200


def test_page_statistics_charge():
    response = client.get('/page/statistics/charge')
    assert response.status_code == 200
