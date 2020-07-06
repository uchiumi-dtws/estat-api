# eStat API Tools

総務省eStatのHPでは、政府統計のデータを公開している。データ取得方法としては

1. eStat HPにアクセスする（or Webスクレイピング）

2. eStat APIを利用する

がある。ここは2の方法についての説明とツール置き場。



### 政府統計コードと統計表ID

eStatで公開されているデータは、「政府統計コード > 統計表ID > No.」 で識別される。たとえば、「平成２７年国勢調査 世界測地系(250Mメッシュ) 　その１　人口等基本集計に関する事項 1次メッシュ　M5035」という表は、「政府統計コード：00200521,  統計表ID：8003001633,  No.：1」である。



データを取得したい政府統計の「政府統計コード」がわかれば、その中に含まれる統計表を条件検索できる。条件検索する際にも参照するIDをここに記す。

- [政府統計コード一覧](https://www.e-stat.go.jp/help/stat-search-3-5)（例：「国勢調査2015」= "00200521"）
- [統計表の作成機関コード](https://www.stat.go.jp/info/guide/public/code/pdf/code.pdf)（例：「総務省」= "00200"）
- [都道府県コード、市区町村コード](https://www.soumu.go.jp/denshijiti/code.html)（例：「北海道」="01"「札幌市」= "1002 "）
- [全国地方公共団体コード](https://www.soumu.go.jp/denshijiti/code.html)（例：：「北海道札幌市」= "011002"）



eStat API (version 3.0) の仕様については、[API仕様書 (ver 3.0)](https://www.e-stat.go.jp/api/api-info/e-stat-manual3-0) を参照。



### Usage (workflow)



**step 0：eStat API のアプリケーションIDを取得する。**

[eStats API](https://www.e-stat.go.jp/api/)のトップページにアクセスして、「ユーザ登録・ログイン」から手続きを行う。氏名・メールアドレス・パスワードを登録すると、メールにてアプリケーションIDが送付される。アプリケーションIDがないとAPIコールできない。

**step 1：HTTP GETをコールして、APIからレスポンス（データ）を受け取る。**

APIの細かい使い方は、[API仕様書 (ver 3.0)](https://www.e-stat.go.jp/api/api-info/api-spec) を参照。基本、以下2つのコールができればほとんど困ることはない。



1. 統計情報取得（getStatsList）
   - URLとパラメータを指定して、条件にあうすべての統計表の情報（ID, 名前, その他）を得る。
     - URL：`EstatRestAPI_URLParser()クラス`の`getStatsListURL()メソッド`を使う。[仕様書の2.1](https://www.e-stat.go.jp/api/api-info/e-stat-manual3-0#api_2_1)を見る
     - パラメータ：[仕様書の3.2](https://www.e-stat.go.jp/api/api-info/e-stat-manual3-0#api_3_2)を見る
2. 統計データ取得（getStatsData）
   - URLとパラメータを指定して、条件にあう統計表の生データを得る。
     - URL：`EstatRestAPI_URLParser()クラス`の`getStatsDataURL()メソッド`を使う。[仕様書の2.3](https://www.e-stat.go.jp/api/api-info/e-stat-manual3-0#api_2_3)を見る
     - パラメータ：[仕様書の3.4](https://www.e-stat.go.jp/api/api-info/e-stat-manual3-0#api_3_4)を見る。



サンプルコード：国勢調査(政府統計コード：00200521)のうち検索キーワード「人口等基本集計に関する事項」を含む統計表のリストを取得し、統計表IDを用いて生データをCSVファイルとしてダウンロードする。

```python
import csv
import json
import requests
from estat_api import download_json, EstatRestAPI_URLParser

def get_json(url):
    try:
        print("HTTP GET", url)
        r = requests.get(url)
        json_dict = r.json()
        return json_dict
    except requests.exceptions.RequestException as err:
        print(err)

def download_csv(url, filepath):
    try:
        print("HTTP GET", url)        r = requests.get(url)
        with open(filepath, 'w') as f:
            writer = csv.writer(f)
            for line in r.iter_lines():
                writer.writerow(line.decode('utf-8').split(','))
    except requests.exceptions.RequestException as err:
        print(err)

## Common settings
appId = "65a9e884e72959615c2c7c293ebfaeaebffb6030"  # Application ID
estatapi_url_parser = EstatRestAPI_URLParser() # URL Parser

## 1. 統計情報取得
## call API (GET data as JSON) -> save as python objects (dict)
stats_code = "00200521"
params_dict = {
    "appId": appId,                        # Application ID
    "lang": "J",                           # 言語 (J:日本語, E:英語)
    "surveyYears": 2015,                   # 調査年月 (YYYY or YYYYMM or YYYYMM-YYYYMM)
    "statsCode": stats_code,               # 政府統計コード（8桁)
    "searchKind": "2",                     # 検索データ種別 (1:統計情報, 2:小地域・地域メッシュ)
    "searchWord": "人口等基本集計に関する事項", # 検索キーワード (任意の文字列)
    "explanationGetFlg": "N"               # 解説情報有無 (Y or N)
}
url = estatapi_url_parser.getStatsListURL(params_dict, format="json")
statslist_dict = get_json(url)

## 2. 統計データ取得
## python object (dict) -> search URL -> call API (GET data as CSV) -> save local file
table_list= statslist_dict["GET_STATS_LIST"]["DATALIST_INF"]["TABLE_INF"]
for table in table_list:
    table_id = table["@id"]
    table_name = str(table["STATISTICS_NAME"])+"_"+str(table["TITLE"]["@no"])+"_"+str(table["TITLE"]["$"])
    params_dict = {
        "appId": appId,                # Application ID
        "lang": "J",                   # 言語 (J: 日本語, E: 英語)
        "statsDataId": str(table_id),  # 統計表ID
        "explanationGetFlg": "N",      # 解説情報有無(Y or N)
        "annotationGetFlg": "N",       # 注釈情報有無(Y or N)
    }
    url = estatapi_url_parser.getStatsDataURL(params_dict, format="csv")
    filepath = f"./data/{stats_code}_{table_id}_{table_name}.csv"
    download_csv(url, filepath)
```



**step 2：Cloud Strage, BigQueryに保存**

取得した生データ（CSVファイル）を加工して、GCP上にアップロードする。





