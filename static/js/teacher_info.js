j = {
    "type": "page",
    "title": "教师信息",
    "body": [{
        "type": "tpl",
        "tpl": '你可以在此处通过上传Excel文件来批量导入教师姓名信息，也可以通过在下方表格中点击 新增 按钮来新增教师',
        "inline": false
    }, {
        "type": "tpl",
        "tpl": '此系统通过教师名称来识别教师，因此对于同名教师请通过在姓名中增加其他内容来进行区别',
        "inline": false
    },
    //{
    //     "type": "tpl",
    //     "tpl": '系统会自动解析上传的Excel文件，将该文件中所有sheet中所有有内容的且不以',
    //     "inline": true
    // }, {
    //     "type": "tpl",
    //     "tpl": '#',
    //     "style": {
    //         "color": "#f8e71c",
    //         "backgroundColor": "#000000"
    //     },
    //     "inline": true
    // }, {
    //     "type": "tpl",
    //     "tpl": '开头的单元格识别为一个教师姓名，并且进行存储',
    //     "inline": true
    // },
    // {
    //     "type": "tpl",
    //     "tpl": '以#开头的单元格会被识别为注释单元格，你可以通过这种方式来为文档添加一些额外的说明信息',
    //     "inline": false
    // },
    // {
    //     "type": "tpl",
    //     "tpl": '所有sheet均会被解析，因此你可以通过创建不同的sheet来为教师进行分类',
    //     "inline": false
    // },
    {
        "type": "form",
        "title": "教师名单上传",
        "api": "put:" + config_url + ":" + config_port + "/data/teacher_info/file",
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
    }, {
        "type": "tpl",
        "tpl": '你可以在此处通过上传Excel文件来批量导入教师课表信息，后导入的课表会将先前课表覆盖',
        "inline": false
    }, {
        "type": "tpl",
        "tpl": '系统会对上传的Excel文件的所有sheet进行解析，来获取课程表信息',
        "inline": false
    },
    // {
    //     "type": "tpl",
    //     "tpl": '当某一单元格内容为',
    //     "inline": true
    // },
    // {
    //     "type": "tpl",
    //     "tpl": '教师：xxx',
    //     "style": {
    //         "color": "#f8e71c",
    //         "backgroundColor": "#000000"
    //     },
    //     "inline": true
    // },
    // {
    //     "type": "tpl",
    //     "tpl": '时，到下一个此类单元格出现，或者该sheet结束，系统会自动把后续可能的课程表条目解析，并设置到该教师名下，因此要求对教师的说明信息需要在课程表内容之前出现',
    //     "inline": true
    // },
    // {
    //     "type": "tpl",
    //     "tpl": '',
    //     "inline": false
    // },
    // {
    //     "type": "tpl",
    //     "tpl": '当系统扫描到某一单元格中包含形如',
    //     "inline": true
    // },
    // {
    //     "type": "tpl",
    //     "tpl": '小时:分钟-小时:分钟',
    //     "style": {
    //         "color": "#f8e71c",
    //         "backgroundColor": "#000000"
    //     },
    //     "inline": true
    // },
    // {
    //     "type": "tpl",
    //     "tpl": '格式的内容时，就会将该单元格视为已经识别到的教师下的一个时间段，并且将该单元格同一行后面的7个包含不以',
    //     "inline": true
    // }, {
    //     "type": "tpl",
    //     "tpl": '#',
    //     "style": {
    //         "color": "#f8e71c",
    //         "backgroundColor": "#000000"
    //     },
    //     "inline": true
    // }, {
    //     "type": "tpl",
    //     "tpl": '开头的单元格识别为该教师在这周的这个时间段有课',
    //     "inline": true
    // },
    // {
    //     "type": "tpl",
    //     "tpl": '',
    //     "inline": false
    // },
    // {
    //     "type": "tpl",
    //     "tpl": '但请注意，有内容的单元格只会被识别为占位，即不会在这个时间段给该老师排考，但是不一定参与课时统计。如果想让某个单元格参与课时统计，该单元格需要包含形如',
    //     "inline": true
    // }, {
    //     "type": "tpl",
    //     "tpl": '高x',
    //     "style": {
    //         "color": "#f8e71c",
    //         "backgroundColor": "#000000"
    //     },
    //     "inline": true
    // }, {
    //     "type": "tpl",
    //     "tpl": '（x可以为一、二或三）的字符串',
    //     "inline": true
    // },
    // {
    //     "type": "tpl",
    //     "tpl": '',
    //     "inline": false
    // },
    // {
    //     "type": "tpl",
    //     "tpl": '在解析过程中会将该教师是否在某个年级任教自动确定，在多个年级任教的教师会根据课程所属年级不同自动统计课时数',
    //     "inline": false
    // }, {
    //     "type": "tpl",
    //     "tpl": '教师课表只能通过文件上传，并且后上传的课表会覆盖之前的课表（即更新操作），当教师不存在时将无法成功更新',
    //     "inline": false
    // },
    {
        "type": "form",
        "title": "教师课程表上传",
        "api": "put:" + config_url + ":" + config_port + "/data/teacher_coursetable_info/file",
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
    },
    {
        "type": "crud",
        "api": "get:" + config_url + ":" + config_port + "/data/teacher_info",
        "source": "${items | filter:teacher_name:match:keywords}",
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
                "type": "crud",
                "label": "教师课表",
                "api": config_url + ":" + config_port + "/data/teacher_info/course_items?teacher_name=${teacher_name}",
                "primaryField": "time_segment",
                "syncLocation": false,
                "loadDataOnce": true,
                "headerToolbar": [
                    "bulkActions",
                    "pagination"
                ],
                "columns": [
                    {
                        "name": "time_segment",
                        "label": "时间段",
                        "type": "text"
                    }, {
                        "name": "day1",
                        "label": "周一",
                        "type": "text"
                    }, {
                        "name": "day2",
                        "label": "周二",
                        "type": "text"
                    }, {
                        "name": "day3",
                        "label": "周三",
                        "type": "text"
                    }, {
                        "name": "day4",
                        "label": "周四",
                        "type": "text"
                    }, {
                        "name": "day5",
                        "label": "周五",
                        "type": "text"
                    }, {
                        "name": "day6",
                        "label": "周六",
                        "type": "text"
                    }, {
                        "name": "day7",
                        "label": "周日",
                        "type": "text"
                    }]
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
                            "url": config_url + ":" + config_port + "/data/teacher_info",
                            "data": {
                                "teacher_name": "${teacher_name}"
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
                    "url": "/data/teacher_info/${ids|raw}"
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
                        "api": "put:" + config_url + ":" + config_port + "/data/teacher_info",
                        "body": [
                            {
                                "type": "input-text",
                                "name": "teacher_name",
                                "label": "教师名称"
                            },
                            {
                                "type": "input-text",
                                "name": "extra_hour",
                                "label": "额外课时数",
                                "value": "0"
                            }, {
                                "name": "is_duty",
                                "type": "checkbox",
                                "option": "两处人员"
                            }, {
                                "name": "is_charge",
                                "type": "checkbox",
                                "option": "行政人员"
                            }
                        ]
                    }
                }
            },
            "bulkActions",
            "pagination"
        ],
        "defaultParams": {
            "perPage": 6
        },
        "messages": {
        },
        "primaryField": "teacher_name",
        "syncLocation": true
        // "loadDataOnce": true
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