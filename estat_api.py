import json
import urllib
import requests


def download_json(save_file, url):
    try:
        print("HTTP GET", url)
        r = requests.get(url)
        d = r.json()
        s = json.dumps(d, indent=2, ensure_ascii=False)
        with open(save_file, 'w') as f:
            f.write(s)
    except requests.exceptions.RequestException as err:
        print(err)


class EstatRestAPI_URLParser():

    def __init__(self):
        self.api_version = "3.0"
        self.app_id = "65a9e884e72959615c2c7c293ebfaeaebffb6030"  # アプリケーションID

    def getStatsListURL(self, params_dict, format="csv"):
        """
        2.1 統計表情報取得 (HTTP GET)
        """
        params_str = urllib.parse.urlencode(params_dict)
        if format == "xml":
            url = f"https://api.e-stat.go.jp/rest/{self.api_version}/app/getStatsList?{params_str}"
        elif format == "json":
            url = f"https://api.e-stat.go.jp/rest/{self.api_version}/app/json/getStatsList?{params_str}"
        elif format == "jsonp":
            url = f"https://api.e-stat.go.jp/rest/{self.api_version}/app/jsonp/getStatsList?{params_str}"
        elif format == "csv":
            url = f"https://api.e-stat.go.jp/rest/{self.api_version}/app/getSimpleStatsList?{params_str}"
        return url

    def getMetaInfoURL(self, params_dict, format="csv"):
        """
        2.2 メタ情報取得 (HTTP GET)
        """
        params_str = urllib.parse.urlencode(params_dict)
        if format == "xml":
            url = f"https://api.e-stat.go.jp/rest/{self.api_version}/app/getMetaInfo?{params_str}"
        elif format == "json":
            url = f"https://api.e-stat.go.jp/rest/{self.api_version}/app/json/getMetaInfo?{params_str}"
        elif format == "jsonp":
            url = f"https://api.e-stat.go.jp/rest/{self.api_version}/app/jsonp/getMetaInfo?{params_str}"
        elif format == "csv":
            url = f"https://api.e-stat.go.jp/rest/{self.api_version}/app/getSimpleMetaInfo?{params_str}"
        return url

    def getStatsDataURL(self, params_dict, format="csv"):
        """
        2.3 統計データ取得 (HTTP GET)
        """
        params_str = urllib.parse.urlencode(params_dict)
        if format == "xml":
            url = f"https://api.e-stat.go.jp/rest/{self.api_version}/app/getStatsData?{params_str}"
        elif format == "json":
            url = f"https://api.e-stat.go.jp/rest/{self.api_version}/app/json/getStatsData?{params_str}"
            self.save_json(save_file, url)
            return
        elif format == "jsonp":
            url = f"https://api.e-stat.go.jp/rest/{self.api_version}/app/jsonp/getStatsData?{params_str}"
        elif format == "csv":
            url = f"https://api.e-stat.go.jp/rest/{self.api_version}/app/getSimpleStatsData?{params_str}"
        return url

    def postDatasetURL(self):
        """
        2.4 データセット登録 (HTTP POST)
        """
        url = f"http(s)://api.e-stat.go.jp/rest/{self.api_version}/app/postDataset"
        return url

    def refDataset(self, params_dict, format="xml"):
        """
        2.5 データセット参照 (HTTP GET)
        """
        params_str = urllib.parse.urlencode(params_dict)
        if format == "xml":
            url = f"http(s)://api.e-stat.go.jp/rest/{self.api_version}/app/refDataset?{params_str}"
        elif format == "json":
            url = f"http(s)://api.e-stat.go.jp/rest/{self.api_version}/app/json/refDataset?{params_str}"
        elif format == "jsonp":
            url = f"http(s)://api.e-stat.go.jp/rest/{self.api_version}/app/jsonp/refDataset?{params_str}"
        return url

    def getDataCatalogURL(self, params_dict, format="xml"):
        """
        2.6 データカタログ情報取得 (HTTP GET)
        """
        params_str = urllib.parse.urlencode(params_dict)
        if format == "xml":
            url = f"http(s)://api.e-stat.go.jp/rest/{self.api_version}/app/getDataCatalog?{params_str}"
        elif format == "json":
            url = f"http(s)://api.e-stat.go.jp/rest/{self.api_version}/app/json/getDataCatalog?{params_str}"
        elif format == "jsonp":
            url = f"http(s)://api.e-stat.go.jp/rest/{self.api_version}/app/jsonp/getDataCatalog?{params_str}"
        return url

    def getStatsDatasURL(self, params_dict, format="xml"):
        """
        2.7 統計データ一括取得 (HTTP GET)
        """
        params_str = urllib.parse.urlencode(params_dict)
        if format == "xml":
            url = f"http(s)://api.e-stat.go.jp/rest/{self.api_version}/app/getStatsDatas?{params_str}"
        elif format == "json":
            url = f"http(s)://api.e-stat.go.jp/rest/{self.api_version}/app/json/getStatsDatas?{params_str}"
        elif format == "csv":
            url = f"http(s)://api.e-stat.go.jp/rest/{self.api_version}/app/getSimpleStatsDatas?{params_str}"
        return url
