import imp
from pydantic import BaseModel
from typing import Optional


class Result(BaseModel):
    status: int = 0
    msg: str = ''
    data: Optional[dict] = {}


class TimeStr():

    def __init__(self, time_str: str):
        time_list = time_str.split(':')
        self.hour = int(time_list[0])
        if self.hour >= 24 or self.hour < 0:
            raise Exception('TimeStr构造失败：不合法的小时' + str(self.hour))
        self.min = int(time_list[1])
        if self.min >= 60 or self.hour < 0:
            raise Exception('TimeStr构造失败：不合法的分钟' + str(self.min))

    def __str__(self):
        r: str = ''
        if len(str(self.hour)) == 1:
            r += '0'
        r += str(self.hour)
        r += ':'
        if len(str(self.min)) == 1:
            r += '0'
        r += str(self.min)
        return r
