j = {
    "type": "page",
    "title": "两处数据统计",
    "body": [
        {
            "type": "tpl",
            "tpl": "两处教师贡献统计结果",
            "inline": false
        },
        {
            "type": "crud",
            "api": "get:" + config_url + ":" + config_port + "/data/statistics/duty",
            "source": "${items | filter:teacher_name:match:keywords}",
            "defaultParams": {
                "perPage": 50
            },
            "filter": {
                "body": [
                    {
                        "type": "input-text",
                        "name": "keywords",
                        "label": "教师名称"
                    }
                ]
            },
            "columns": [
                {
                    "name": "teacher_name",
                    "label": "教师名称",
                    "type": "text"
                }, {
                    "name": "exam_hour",
                    "label": "行政监考时间",
                    "type": "text"
                }
            ],

            "itemActions": [
            ],
            "features": [
                "create",
                "filter",
                "bulkDelete",
                "delete"
            ],
            "headerToolbar": [
                {
                    "type": "export-excel",
                    "label": "导出 Excel"

                },
                "pagination"
            ],
            "perPageAvailable": [
                10
            ],
            "messages": {
            },
            "primaryField": "teacher_name",
            "syncLocation": false,
            "loadDataOnce": true
        },
        {
            "type": "chart",
            "api": config_url + ":" + config_port + "/data/statistics/duty_hour_charts"
        }
    ],
    "toolbar": [{
        "type": "button",
        "label": "返回上一级",
        "actionType": "url",
        "dialog": {
            "title": "系统提示",
            "body": "对你点击了"
        },
        "size": "lg",
        "level": "warning",
        "url": config_url + ":" + config_port + "/page/statistics_select",
        "blank": false,
        "className": "m"
    }, {
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