import os
import webbrowser
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from scheduler.routers.data.db_manage import models
from scheduler.routers.data.db_manage.database import engine

from scheduler.routers.page.page_common import config

data_path = './user_data'
if not os.path.exists(data_path):
    os.mkdir(data_path)

models.Base.metadata.create_all(bind=engine)

from scheduler.routers.page import router as page_router
from scheduler.routers.data import router as data_router

import uvicorn as u

app = FastAPI()
app.include_router(page_router)
app.include_router(data_router)

app.mount("/static", StaticFiles(directory=os.getcwd()+"/static"), name="static")


# 重定向到首页
@app.get("/")
async def redirect():
    return RedirectResponse('/page/index')


if __name__ == '__main__':
    log_config = u.config.LOGGING_CONFIG
    if not config['debug']:
        log_config['handlers'] = {
            "default": {
                "formatter": "default",
                "class": "logging.handlers.TimedRotatingFileHandler",
                "filename": data_path + '/' + 'scheduler.log'
            },
            "access": {
                "formatter": "access",
                "class": "logging.handlers.TimedRotatingFileHandler",
                "filename": data_path + '/' + 'scheduler.log'
            },
        }
    print('请使用谷歌或火狐浏览器（不支持IE）访问网址：' + config['url'] + ':' + str(config['port']) + ' 来使用排考系统')
    webbrowser.open_new(config['url'] + ':' + str(config['port']))
    u.run(app, host="127.0.0.1", port=5700, log_config=log_config)
