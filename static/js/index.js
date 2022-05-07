let j = {
    "type": "page",
    "title": "首页",
    "body": [
        {
            "type": "button",
            "label": "数据上传",
            "actionType": "url",
            "dialog": {
                "title": "系统提示",
                "body": "对你点击了"
            },
            "size": "lg",
            "level": "primary",
            "block": true,
            "blank": false,
            "url": "http://127.0.0.1:5700/page/upload"
        },
        {
            "type": "button",
            "label": "教师信息查询",
            "actionType": "url",
            "dialog": {
                "title": "系统提示",
                "body": "对你点击了"
            },
            "size": "lg",
            "level": "light",
            "block": true,
            "url": "http://127.0.0.1:5700/page/teacher_info_query",
            "blank": false
        },
        {
            "type": "button",
            "label": "创建考试",
            "actionType": "url",
            "dialog": {
                "title": "系统提示",
                "body": "对你点击了"
            },
            "size": "lg",
            "level": "dark",
            "block": true,
            "url": "http://127.0.0.1:5700/page/create_exam",
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
            "url": "http://127.0.0.1:5700/page/exam_list",
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
            "url": "http://127.0.0.1:5700/page/statistics",
            "size": "lg",
            "level": "danger",
            "block": true
        }
    ]
};