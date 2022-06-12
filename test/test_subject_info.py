from fastapi.testclient import TestClient

import sys

sys.path.append('D:\\大四下\\毕业设计\\虚拟环境fastapi\\scheduler')

from scheduler.main import app

client = TestClient(app)


def test_subject_info_get():
    response = client.get('/data/subject_info?page=1')
    assert response.status_code == 200
    assert response.json() == {
        "status": 0,
        "msg": "",
        "data": {
            "items": [{
                "subject_name": "化学"
            }, {
                "subject_name": "语文"
            }, {
                "subject_name": "物理"
            }, {
                "subject_name": "数学"
            }, {
                "subject_name": "政治"
            }, {
                "subject_name": "历史"
            }, {
                "subject_name": "英语"
            }, {
                "subject_name": "信息科技"
            }]
        }
    }


def test_subject_info_put_delete():
    response = client.put('/data/subject_info', json={"subject_name": "测试"})
    assert response.status_code == 200
    assert response.json() == {"status": 0, "msg": "", "data": {}}
    response = client.delete('/data/subject_info', json={"subject_name": "测试"})
    assert response.status_code == 200
    assert response.json() == {"status": 0, "msg": "", "data": {}}


def test_subject_info_batch_delete():
    client.put('/data/subject_info', json={"subject_name": "测试"})
    response = client.delete('/data/subject_info/测试')
    assert response.status_code == 200
    assert response.json() == {"status": 0, "msg": "", "data": {}}
