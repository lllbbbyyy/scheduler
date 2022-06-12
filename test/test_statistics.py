from fastapi.testclient import TestClient

import requests
from io import BytesIO

from requests_toolbelt import MultipartEncoder

import sys

sys.path.append('D:\\大四下\\毕业设计\\虚拟环境fastapi\\scheduler')

from scheduler.main import app

client = TestClient(app)


def test_statistics_get():
    response = client.get('/data/statistics?grade=高一&page=1')
    assert response.status_code == 200

def test_class_hour_charts():
    response = client.get('/data/statistics/class_hour_charts?grade=高一')
    assert response.status_code == 200

def test_exam_hour_charts():
    response = client.get('/data/statistics/exam_hour_charts?grade=高一')
    assert response.status_code == 200

def test_all_contribution_charts():
    response = client.get('/data/statistics/all_contribution_charts?grade=高一')
    assert response.status_code == 200

def test_duty_hour_charts():
    response = client.get('/data/statistics/duty_hour_charts')
    assert response.status_code == 200

def test_duty():
    response = client.get('/data/statistics/duty?page=1')
    assert response.status_code == 200

def test_charge_hour_charts():
    response = client.get('/data/statistics/charge_hour_charts')
    assert response.status_code == 200

def test_charge():
    response = client.get('/data/statistics/charge?page=1')
    assert response.status_code == 200