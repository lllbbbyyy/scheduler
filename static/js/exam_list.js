j = {
    "type": "page",
    "title": "考试列表",
    "body": [
        {
            "type": "crud",
            "api": "get:" + config_url + ":" + config_port + "/data/exam_info",
            "defaultParams": {
                "perPage": 50
            },
            "columns": [
                {
                    "name": "exam_id",
                    "label": "考试编号",
                    "type": "text"
                },
                {
                    "name": "exam_name",
                    "label": "考试名称",
                    "type": "text"
                }, {
                    "name": "exam_create_time",
                    "label": "考试创建时间",
                    "type": "text"
                },
                {
                    "type": "crud",
                    "label": "排考表",
                    "api": config_url + ":" + config_port + "/data/exam_info/scheduled_items?exam_id=${exam_id}",
                    "quickSaveApi": "post:" + config_url + ":" + config_port + "/data/exam_info/scheduled_items?exam_id=${exam_id}",
                    "combineNum": 1,
                    "primaryField": "time_segment",
                    "syncLocation": false,
                    "loadDataOnce": true,

                    "headerToolbar": [
                        "bulkActions",
                        "pagination",
                        {
                            "type": "export-excel",
                            "label": "导出 Excel"
                        }
                    ]
                }
                ,
                {
                    "type": "operation",
                    "label": "操作",
                    "buttons": [
                        {
                            "type": "button",
                            "label": "删除",
                            "actionType": "ajax",
                            "level": "link",
                            "className": "text-danger",
                            "confirmText": "确定要删除？",
                            "api": {
                                "method": "delete",
                                "url": config_url + ":" + config_port + "/data/exam_info",
                                "data": {
                                    "exam_id": "${exam_id}"
                                }
                            }
                        }
                    ]
                }
            ],
            "bulkActions": [
                {
                    "type": "button",
                    "level": "danger",
                    "label": "批量删除",
                    "actionType": "ajax",
                    "confirmText": "确定要删除？",
                    "api": {
                        "method": "delete",
                        "url": "/data/exam_info/${ids|raw}"
                    }
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
                "bulkActions",
                "pagination"
            ],
            "perPageAvailable": [
                10
            ],
            "messages": {
            },
            "primaryField": "exam_id",
            "syncLocation": false,
            "loadDataOnce": true
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