#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests,os,sys
import json
from bs4 import BeautifulSoup

# 設定 Header 
headers = {
    "Accept": "*/*",
    "Accept-Language": 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6',
    "DNT": "1",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Content-Type":"application/json; charset=UTF-8",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3573.0 Safari/537.36",
    }


selcode = input(str("輸入選課代碼："))

payload = {
    "baseOptions":{ 
        "lang":"cht",
        "year":"108",
        "sms":"2"
        },
    "typeOptions":{
        "code":{             # 選課代號
            "enabled":"true",
            "value":selcode
            },
        "weekPeriod":{
            "enabled":"false",
            "week":"*",      # 星期 */1/2/../7
            "period":"*"     # 節次 */0/1/2/../14
            },
        "course":{           # 科目名稱
            "enabled":"false",
            "value":""
            },
        "teacher":{          # 開課教師姓名
            "enabled":"false",
            "value":""
            },
        "useEnglish":{       # 全英語授課
            "enabled":"false"
            },
        "useLanguage":{      # 授課語言
            "enabled":"false",
            "value":"01"     # 01：中文 02：英語 03：日語 04：德語 05：法語 06：西班牙語 07：其他 08：中英
            },
        "specificSubject":{  # 特定科目
            "enabled":"false",
            "value":"1"      # 1：通識課程 2：體育選項課程 3：大學國文
            },
        "courseDescription":{# 課程描述
            "enabled":"false",
            "value":""
            }
        }
    }

payload = json.dumps(payload)

url = "https://coursesearch03.fcu.edu.tw/Service/Search.asmx/GetType2Result"

r = requests.post(url,headers=headers,data = payload)  
r = r.text                                             

r = r.replace('\\"','"' )
r = r.replace(':"{',': {' )
r = r.replace('}]}"}','}]}}')

r = json.loads(r)                                     

print("選課代碼:",r['d']['items'][0]['scr_selcode'])
print("課程編碼:",r['d']['items'][0]['sub_id3'])
print("課程名稱:",r['d']['items'][0]['sub_name'])
print("學分:",r['d']['items'][0]['scr_credit'])
print("必選修:",r['d']['items'][0]['scj_scr_mso'])
print("開課班級:",r['d']['items'][0]['cls_name'])
print("上課時間/上課教室/授課教師:",r['d']['items'][0]['scr_period'])
print("開放名額:",r['d']['items'][0]['scr_precnt'])
print("實收名額:",r['d']['items'][0]['scr_acptcnt'])


# url = "http://service005.sds.fcu.edu.tw/favicon.ico"

# r = requests.Session().post(url)
# r = r.post(url,data = payload)
# soup = BeautifulSoup(r.text, 'lxml') 
# r = soup.find('meta').get('content')
# index = r.find('=') 
# url = r[ index +1 : ]