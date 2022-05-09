import os
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from routers.data.db_manage import models
from routers.data.db_manage.database import engine

models.Base.metadata.create_all(bind=engine)

from routers.page import router as page_router
from routers.data import router as data_router

import uvicorn as u

data_path = './user_data'
if not os.path.exists(data_path):
    os.mkdir(data_path)

app = FastAPI()
app.include_router(page_router)
app.include_router(data_router)

app.mount("/static", StaticFiles(directory="static"), name="static")


# 重定向到首页
@app.get("/")
async def redirect():
    return RedirectResponse('/page/index')


# @app.post("/teacher_class_file_upload")
# def teacher_class_file_upload(teacher_class_file: UploadFile):
#     print(teacher_class_file.filename)
#     contents=teacher_class_file.file.read()
#     with open(teacher_class_file.filename,'wb') as f:
#         f.write(contents)
#     return {"status": 0, "msg": "", "data": {}}

if __name__ == '__main__':
    u.run(app, host="127.0.0.1", port=5700)
