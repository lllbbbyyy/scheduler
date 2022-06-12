let j = {
    "type": "page",
    "title": "首页",
    "body": [
        {
            "type": "button",
            "label": "科目信息",
            "actionType": "url",
            "dialog": {
                "title": "系统提示",
                "body": "对你点击了"
            },
            "size": "lg",
            "block": true,
            "level": "warning",
            "url": "http://127.0.0.1:" + config_port + "/page/subject_info",
            "blank": false
        },
        {
            "type": "button",
            "label": "教师信息",
            "actionType": "url",
            "dialog": {
                "title": "系统提示",
                "body": "对你点击了"
            },
            "size": "lg",
            "block": true,
            "level": "primary",
            "url": config_url + ":" + config_port + "/page/teacher_info",
            "blank": false
        },
        {
            "type": "button",
            "label": "考试列表",
            "actionType": "url",
            "dialog": {
                "title": "系统提示",
                "body": "对你点击了"
            },
            "size": "lg",
            "level": "success",
            "block": true,
            "url": config_url + ":" + config_port + "/page/exam_info",
            "blank": false
        },
        {
            "type": "button",
            "label": "数据统计",
            "actionType": "url",
            "dialog": {
                "title": "系统提示",
                "body": "对你点击了"
            },
            "blank": false,
            "url": config_url + ":" + config_port + "/page/statistics_select",
            "size": "lg",
            "level": "danger",
            "block": true
        }
    ]
};