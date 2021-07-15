      _________                                      _____ __________.___ 
      \_   ___ \  ____  __ _________  ______ ____   /  _  \\______   \   |
      /    \  \/ /  _ \|  |  \_  __ \/  ___// __ \ /  /_\  \|     ___/   |
      \     \___(  <_> )  |  /|  | \/\___ \\  ___//    |    \    |   |   |
       \______  /\____/|____/ |__|  /____  >\___  >____|__  /____|   |___|
              \/                         \/     \/        \/              
- 此專案用來說明[逢甲大學程檢索系統](https://coursesearch03.fcu.edu.tw/)的查詢方式。
- 給有需要查詢或取得課程資訊的人，或是直接取用 [FCU-CourseData](https://github.com/HeiTang/FCU-CourseData) 專案中的資料。

## 查詢格式
### 依開課系所查詢
```json=
{
    "baseOptions":{
        "lang":"cht",
        "year":110,
        "sms":1
    },
    "typeOptions":{
        "degree":"1",            # 學制（1：大學 3：碩士 4：博士 5：進修）
        "deptId":"CC",           # 院所 / 其他
        "unitId":"CC00",         # 系所
        "classId":"CC00100"      # 班級
    }
}
```
- `degree` 、 `deptId` 和 `classId` 參數可以參考 [FCU-ClassID](https://github.com/HeiTang/FCU-ClassID#readme) 。

### 依輸入條件查詢
```json=
{
    "baseOptions":{ 
        "lang":"cht",             # cht：中文 en：英文
        "year":"108",             # 學年度 101~110
        "sms":"2"                 # 1：上學期 2：下學期 3：暑修上 4：暑修下
    },
    "typeOptions":{
        "code":{                  # 選課代號
            "enabled":"true",
            "value":""
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
- `week` 和 `period` 不能同時皆為 `*`。
- `typeOptions` 下若要啟用該搜尋選項，則須將 `enabled` 改為 `True`。

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
                "sub_id3": "IECS203",      # 課程編碼
                "sub_name": "系統程式",     # 課程名稱
                "scr_credit": 3.0,         # 學分
                "scj_scr_mso": "必修",      # 選修
                "scr_examid": "否",
                "scr_examfn": "否",
                "scr_exambf": "否",
                "cls_name": "資訊二丁",      # 開課班級
                "scr_period": "(一)08-09 忠206 (三)07     忠B01 林志敏",      # 上課時間 / 上課教室 / 授課教師
                "scr_precnt": 85.0,         # 開放名額
                "scr_acptcnt": 81.0,        # 實收名額
                "scr_remarks": null,        # 備註
                "unt_ls": 4501, 
                "cls_id": "CE07124",        # 開課班級 ID
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
| scr_period  | 上課時間 / 上課教室 / 授課教師 | (一)08-09 忠206 (三)07     忠B01 林志敏 |	
| scr_precnt  | 開放名額 | 85.0 |
| scr_acptcnt | 實收名額 | 81.0 |
| scr_remarks | 備註 | null |
| unt_ls      | | 4501 |
| cls_id      | 開課班級 ID | CE07124 |
| sub_id      | | 18550 |
| scr_dup     | | 001 |
