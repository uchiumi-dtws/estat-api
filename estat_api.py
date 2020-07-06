import urllib
import requests


class EstatRestAPI():

    def __init__(self):
        self.api_version = "3.0"
        self.app_id = "65a9e884e72959615c2c7c293ebfaeaebffb6030"  # アプリケーションID

    def getStatsList(self, save_file, params_dict, format="csv"):
        """
        2.1 統計表情報取得
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

        try:
            print("HTTP GET", url)
            r = requests.get(url)
            with open(save_file, mode='w') as f:
                f.write(r.text)
        except requests.exceptions.RequestException as err:
            print(err)

    def getMetaInfo(self, save_file, params_dict, format="csv"):
        """
        2.2 メタ情報取得
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

        try:
            print("HTTP GET", url)
            r = requests.get(url)
            with open(save_file, mode='w') as f:
                f.write(r.text)
        except requests.exceptions.RequestException as err:
            print(err)

    def getStatsData(self, save_file, params_dict, format="csv"):
        """
        2.3 統計データ取得
        """
        params_str = urllib.parse.urlencode(params_dict)

        if format == "xml":
            url = f"https://api.e-stat.go.jp/rest/{self.api_version}/app/getStatsData?{params_str}"
        elif format == "json":
            url = f"https://api.e-stat.go.jp/rest/{self.api_version}/app/json/getStatsData?{params_str}"
        elif format == "jsonp":
            url = f"https://api.e-stat.go.jp/rest/{self.api_version}/app/jsonp/getStatsData?{params_str}"
        elif format == "csv":
            url = f"https://api.e-stat.go.jp/rest/{self.api_version}/app/getSimpleStatsData?{params_str}"

        try:
            print("HTTP GET", url)
            r = requests.get(url)
            with open(save_file, mode='w') as f:
                f.write(r.text)
        except requests.exceptions.RequestException as err:
            print(err)

    def postDataset(self, params_dict):
        """
        2.4 データセット登録
        HTTP POST
        """
        params_str = urllib.parse.urlencode(params_dict)
        url = f"http(s)://api.e-stat.go.jp/rest/{self.api_version}/app/postDataset"
        pass

    def refDataset(self, save_file, params_dict, format="csv"):
        """
        2.5 データセット参照
        """

    def getDataCatalog(self):
        """
        2.6 データカタログ情報取得
        """
        pass

    def getStatsDatas(self):
        """
        2.7 統計データ一括取得
        """
        pass
