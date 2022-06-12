j = {
    "type": "page",
    "title": "科目信息",
    "body": [
        {
            "type": "tpl",
            "tpl": '科目信息供提交排考信息时使用，需要进行的排考的科目必须是已有的科目',
            "inline": false
        },
        {
            "type": "crud",
            "api": "get:" + config_url + ":" + config_port + "/data/subject_info",
            "source": "${items | filter:subject_name:match:keywords}",
            "filter": {
                "body": [
                    {
                        "type": "input-text",
                        "name": "keywords",
                        "label": "科目信息"
                    }
                ]
            },
            "columns": [
                {
                    "name": "subject_name",
                    "label": "科目信息",
                    "type": "text",
                },
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
                                "url": config_url + ":" + config_port + "/data/subject_info",
                                "data": {
                                    "subject_name": "${subject_name}"
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
                        "url": "/data/subject_info/${ids|raw}"
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
                {
                    "label": "新增",
                    "type": "button",
                    "actionType": "dialog",
                    "level": "primary",
                    "dialog": {
                        "title": "新增",
                        "body": {
                            "type": "form",
                            "api": "put:" + config_url + ":" + config_port + "/data/subject_info",
                            "body": [
                                {
                                    "type": "input-text",
                                    "name": "subject_name",
                                    "label": "科目信息"
                                }
                            ]
                        }
                    }
                },
                "bulkActions",
                "pagination"
            ],
            "perPageAvailable": [
                10
            ],
            "messages": {
            },
            "primaryField": "subject_name",
            "syncLocation": false,
            "loadDataOnce": true
        }
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
            "level": "danger",
            "blank": false,
            "url": config_url + ":" + config_port + "/page/index",
            "className": "m"
        }
    ]
};