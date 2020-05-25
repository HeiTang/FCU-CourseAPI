## 查詢格式
```json=
{
    "baseOptions":{ 
        "lang":"cht",
        "year":"108",
        "sms":"2"
    },
    "typeOptions":{
        "code":{                  # 選課代號
            "enabled":"true",
            "value":selcode
        },
        "weekPeriod":{
            "enabled":"false",
            "week":"*",           # 星期 */1/2/../7
            "period":"*"          # 節次 */0/1/2/../14
        },
        "course":{                # 科目名稱
            "enabled":"false",
            "value":""
        },
        "teacher":{               # 開課教師姓名
            "enabled":"false",
            "value":""
        },
        "useEnglish":{            # 全英語授課
            "enabled":"false"
        },
        "useLanguage":{           # 授課語言
            "enabled":"false",
            "value":"01"          # 01：中文 02：英語 03：日語 04：德語 05：法語 06：西班牙語 07：其他 08：中英
        },
        "specificSubject":{       # 特定科目
            "enabled":"false",
            "value":"1"           # 1：通識課程 2：體育選項課程 3：大學國文
        },
        "courseDescription":{     # 課程描述
            "enabled":"false",
            "value":""
        }
    }
}
```

## Response 格式
> 修正部分格式，使其成為合法 JSON
```json=
{
    "d": {
        "message": "",
        "total": 1,
        "items": [
            {
                "scr_selcode": "1318",     # 課程代碼
                "sub_id3": "IECS203",      #
                "sub_name": "系統程式",     # 
                "scr_credit": 3.0,
                "scj_scr_mso": "必修",
                "scr_examid": "否",
                "scr_examfn": "否",
                "scr_exambf": "否",
                "cls_name": "資訊二丁",
                "scr_period": "(一)08-09 忠206 (三)07     忠B01 林志敏",
                "scr_precnt": 85.0,
                "scr_acptcnt": 81.0,
                "scr_remarks": null,
                "unt_ls": 4501,
                "cls_id": "CE07124",
                "sub_id": "18550",
                "scr_dup": "001"
            }
        ]
    }
}

```
|             |  說明  | 舉例 |
| :---------: | :---: | ---- |
| scr_selcode | 課程代碼 | 1318 |
| sub_id3     | 課程編碼 | IECS203 |
| sub_name    | 課程名稱 | 系統程式 |
| scr_credit  | 學分 | 3.0 |
| scj_scr_mso | 選修 | 必修 |
| scr_examid  | | 否 |
| scr_examfn  | | 否 |
| scr_exambf  | | 否 |
| cls_name    | 開課班級 | 資訊二丁 |
| scr_period  | 上課時間/上課教室/授課教師 | (一)08-09 忠206 (三)07     忠B01 林志敏 |	
| scr_precnt  | 開放名額 | 85.0 |
| scr_acptcnt | 實收名額 | 81.0 |
| scr_remarks | 備註 | null |
| unt_ls      | | 4501 |
| cls_id      | 開課班級 ID | CE07124 |
| sub_id      | | 18550 |
| scr_dup     | | 001 |