j = {
    "type": "page",
    "title": "科目信息",
    "body": [
        {
            "type": "crud",
            "api": "get:http://127.0.0.1:5700/data/subject_info",
            "columns": [
                {
                    "name": "subject_name",
                    "label": "科目信息",
                    "type": "text"
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
                                "url": "http://127.0.0.1:5700/data/subject_info",
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
                            "api": "post:http://127.0.0.1:5700/data/subject_info",
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
        },
        {
            "type": "button",
            "label": "返回上一级",
            "actionType": "url",
            "dialog": {
                "title": "系统提示",
                "body": "对你点击了"
            },
            "size": "lg",
            "level": "primary",
            "url": "http://127.0.0.1:5700/page/upload",
            "blank": false,
            "className": "m"
        },
        {
            "type": "button",
            "label": "返回主页",
            "actionType": "url",
            "dialog": {
                "title": "系统提示",
                "body": "对你点击了"
            },
            "size": "lg",
            "level": "primary",
            "blank": false,
            "url": "http://127.0.0.1:5700/page/index",
            "className": "m"
        }
    ],
    "toolbar": [
    ]
};