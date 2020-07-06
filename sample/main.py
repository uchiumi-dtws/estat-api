import sys
sys.path.append('..')
import csv
import json
import requests
from pprint import pprint
from estat_api import download_json, EstatRestAPI_URLParser

def get_json(url):
    try:
        print("HTTP GET", url)
        r = requests.get(url)
        json_dict = r.json()
        return json_dict
    except requests.exceptions.RequestException as err:
        print(err)


def download_json(url, filepath):
    try:
        print("HTTP GET", url)
        r = requests.get(url)
        json_dict = r.json()
        json_str = json.dumps(json_dict, indent=2, ensure_ascii=False)
        with open(filepath, "w") as f:
            f.write(json_str)
    except requests.exceptions.RequestException as err:
        print(err)


def download_csv(url, filepath):
    try:
        print("HTTP GET", url)
        r = requests.get(url)
        with open(filepath, 'w') as f:
            writer = csv.writer(f)
            for line in r.iter_lines():
                writer.writerow(line.decode('utf-8').split(','))
    except requests.exceptions.RequestException as err:
        print(err)

## Common settings
appId = "65a9e884e72959615c2c7c293ebfaeaebffb6030"  # Application ID
estatapi_url_parser = EstatRestAPI_URLParser() # URL Parser

## 統計情報取得 
## call API (GET data as JSON) -> save as python objects (dict)
stats_code = "00200521"
params_dict = {
    "appId": appId,           # Application ID
    "lang": "J",              # 言語 (J:日本語, E:英語)
    "surveyYears": 2015,      # 調査年月 (YYYY or YYYYMM or YYYYMM-YYYYMM)
    "statsCode": stats_code,  # 政府統計コード（8桁)
    "searchKind": "2",        # 検索データ種別 (1:統計情報, 2:小地域・地域メッシュ)
    "searchWord": "人口等基本集計に関する事項",
    "explanationGetFlg": "N"  # 解説情報有無 (Y or N)
}
url = estatapi_url_parser.getStatsListURL(params_dict, format="json")
statslist_dict = get_json(url)

## 統計データ取得 
## python object (dict) -> search URL -> call API (GET data as CSV) -> save local file
table_list= statslist_dict["GET_STATS_LIST"]["DATALIST_INF"]["TABLE_INF"]
for table in table_list:
    table_id = table["@id"]
    table_name = str(table["STATISTICS_NAME"])+"_"+str(table["TITLE"]["@no"])+"_"+str(table["TITLE"]["$"])
    params_dict = {
        "appId": appId,               # Application ID
        "lang": "J",                  # 言語 (J: 日本語, E: 英語)
        "statsDataId": str(table_id), # 統計表ID
        "explanationGetFlg": "N",     # 解説情報有無(Y or N)
        "annotationGetFlg": "N",      # 注釈情報有無(Y or N)
    }
    url = estatapi_url_parser.getStatsDataURL(params_dict, format="csv")
    filepath = f"./data/{stats_code}_{table_id}_{table_name}.csv"
    download_csv(url, filepath)

