from estat_api import EstatRestAPI


appId = "65a9e884e72959615c2c7c293ebfaeaebffb6030"  # アプリケーションID

params_dict = {
    "appId": appId,
    "lang": "J",  # J: 日本語, E: 英語
    "statsCode": "00200521",  # 政府統計コード（8桁)
    "searchKind": "2",  # 1:統計情報, 2:小地域・地域メッシュ
}
api = EstatRestAPI()
api.getStatsList("main.json", params_dict, format="json")
