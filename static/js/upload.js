let j = {
    "type": "page",
    "title": "数据上传",
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
            "url": "http://127.0.0.1:5700/page/subject_upload",
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
            "url": "http://127.0.0.1:5700/page/teacher_info_upload",
            "blank": false
        },
        {
            "type": "button",
            "label": "教师课程表信息",
            "actionType": "url",
            "dialog": {
                "title": "系统提示",
                "body": "对你点击了"
            },
            "block": true,
            "size": "lg",
            "level": "success",
            "url": "http://127.0.0.1:5700/page/teacher_coursetable_upload",
            "blank": false
        }
    ],
    "aside": [
    ],
    "toolbar": [
        {
            "type": "button",
            "label": "返回主页",
            "actionType": "url",
            "dialog": {
                "title": "系统提示",
                "body": "对你点击了"
            },
            "size": "lg",
            "block": false,
            "level": "primary",
            "url": "http://127.0.0.1:5700/page/index",
            "blank": false
        }
    ]
};