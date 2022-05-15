let j = {
    "type": "page",
    "title": "首页",
    "body": [
        {
            "type": "button",
            "label": "高一数据统计",
            "actionType": "url",
            "dialog": {
                "title": "系统提示",
                "body": "对你点击了"
            },
            "size": "lg",
            "level": "primary",
            "block": true,
            "blank": false,
            "url": config_url + ":" + config_port + "/page/statistics?grade=高一"
        },
        {
            "type": "button",
            "label": "高二数据统计",
            "actionType": "url",
            "dialog": {
                "title": "系统提示",
                "body": "对你点击了"
            },
            "size": "lg",
            "level": "light",
            "block": true,
            "url": config_url + ":" + config_port + "/page/statistics?grade=高二",
            "blank": false
        },
        {
            "type": "button",
            "label": "高三数据统计",
            "actionType": "url",
            "dialog": {
                "title": "系统提示",
                "body": "对你点击了"
            },
            "size": "lg",
            "level": "success",
            "block": true,
            "url": config_url + ":" + config_port + "/page/statistics?grade=高三",
            "blank": false
        }, {
            "type": "button",
            "label": "两处数据统计",
            "actionType": "url",
            "dialog": {
                "title": "系统提示",
                "body": "对你点击了"
            },
            "size": "lg",
            "level": "warning",
            "block": true,
            "url": config_url + ":" + config_port + "/page/statistics/duty",
            "blank": false
        },{
            "type": "button",
            "label": "行政数据统计",
            "actionType": "url",
            "dialog": {
                "title": "系统提示",
                "body": "对你点击了"
            },
            "size": "lg",
            "level": "danger",
            "block": true,
            "url": config_url + ":" + config_port + "/page/statistics/charge",
            "blank": false
        }
    ],
    "toolbar": [{
        "type": "button",
        "label": "返回主页",
        "actionType": "url",
        "dialog": {
            "title": "系统提示",
            "body": "对你点击了"
        },
        "size": "lg",
        "level": "danger",
        "blank": false,
        "url": config_url + ":" + config_port + "/page/index",
        "className": "m"
    }
    ]
};