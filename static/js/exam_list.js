j = {
    "type": "page",
    "title": "考试列表",
    "body": [
        {
            "type": "crud",
            "api": "get:" + config_url + ":" + config_port + "/data/exam_info",
            "source": "${items | filter:exam_name:match:keywords}",
            "filter": {
                "body": [
                    {
                        "type": "input-text",
                        "name": "keywords",
                        "label": "考试名称"
                    }
                ]
            },
            "defaultParams": {
                "perPage": 1
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
                    "defaultParams": {
                        "perPage": 100
                    },

                    "headerToolbar": [
                        "bulkActions",
                        "pagination",
                        {
                            "type": "export-excel",
                            "label": "导出 Excel"
                        }
                    ]
                }
                , {
                    "type": "crud",
                    "label": "两处排考表",
                    "api": config_url + ":" + config_port + "/data/exam_info/scheduled_duty_items?exam_id=${exam_id}",
                    "quickSaveApi": "post:" + config_url + ":" + config_port + "/data/exam_info/scheduled_duty_items?exam_id=${exam_id}",
                    "combineNum": 1,
                    "primaryField": "time_segment",
                    "syncLocation": false,
                    "loadDataOnce": true,
                    "defaultParams": {
                        "perPage": 100
                    },

                    "headerToolbar": [
                        "bulkActions",
                        "pagination",
                        {
                            "type": "export-excel",
                            "label": "导出 Excel"
                        }
                    ]
                }
                , {
                    "type": "crud",
                    "label": "行政排考表",
                    "api": config_url + ":" + config_port + "/data/exam_info/scheduled_charge_items?exam_id=${exam_id}",
                    "quickSaveApi": "post:" + config_url + ":" + config_port + "/data/exam_info/scheduled_charge_items?exam_id=${exam_id}",
                    "combineNum": 1,
                    "primaryField": "time_segment",
                    "syncLocation": false,
                    "loadDataOnce": true,
                    "defaultParams": {
                        "perPage": 100
                    },

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
            "headerToolbar": [{
                "label": "新增考试并进行排考",
                "type": "button",
                "actionType": "dialog",
                "level": "primary",
                "dialog": {
                    "title": "新增考试并进行排考",
                    "body": {
                        "type": "form",
                        "title": "上传",
                        "api": "put:" + config_url + ":" + config_port + "/data/exam_info/file",
                        "body": [
                            {
                                "type": "input-file",
                                "name": "file",
                                "btnLabel": "请选择文件",
                                "accept": ".xlsx",
                                "fileField": "file",
                                "autoUpload": false,
                                "hideUploadButton": true,
                                "asBlob": true,
                                "asBase64": false

                            }
                        ]
                    }
                }
            },
                "bulkActions",
                "pagination"
            ],
            "messages": {
            },
            "primaryField": "exam_id",
            "syncLocation": true
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