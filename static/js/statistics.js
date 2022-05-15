j = {
    "type": "page",
    "title": "数据统计",
    "body": [
        {
            "type": "tpl",
            "tpl": config_grade + "教师贡献统计结果",
            "inline": false
        },
        {
            "type": "crud",
            "api": "get:" + config_url + ":" + config_port + "/data/statistics?grade=" + config_grade,
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
                    "name": "class_contribution",
                    "label": "课时占比系数",
                    "type": "text"
                }, {
                    "name": "exam_contribution",
                    "label": "监考时间占比系数",
                    "type": "text"
                }, {
                    "name": "all_contribution",
                    "label": "贡献系数和",
                    "type": "text"
                }, {
                    "name": "extra_class_num",
                    "label": "班主任/年级主任额外课时数",
                    "type": "text"
                }, {
                    "name": "week_class_num",
                    "label": "周课时数",
                    "type": "text"
                }, {
                    "name": "exam_hour_sum",
                    "label": "监考总时长",
                    "type": "text"
                }
            ],
            "affixRow": [
                [
                    {
                        "type": "text",
                        "text": "总场次"
                    },
                    {
                        "type": "tpl",
                        "tpl": "${exam_all_num}"
                    }
                ],
                [
                    {
                        "type": "text",
                        "text": "总时长"
                    },
                    {
                        "type": "tpl",
                        "tpl": "${exam_all_hour}"
                    }
                ], [
                    {
                        "type": "text",
                        "text": "总人数"
                    },
                    {
                        "type": "tpl",
                        "tpl": "${exam_all_teacher}"
                    }
                ], [
                    {
                        "type": "text",
                        "text": "人均场次"
                    },
                    {
                        "type": "tpl",
                        "tpl": "${exam_arr_num}"
                    }
                ], [
                    {
                        "type": "text",
                        "text": "人均时长"
                    },
                    {
                        "type": "tpl",
                        "tpl": "${exam_arr_hour}"
                    }
                ]
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
            "api": config_url + ":" + config_port + "/data/statistics/class_hour_charts?grade=" + config_grade
        },
        {
            "type": "chart",
            "api": config_url + ":" + config_port + "/data/statistics/exam_hour_charts?grade=" + config_grade
        },
        {
            "type": "chart",
            "api": config_url + ":" + config_port + "/data/statistics/all_contribution_charts?grade=" + config_grade
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