import csv
import json
import requests


def get_json(url):
    try:
        print("HTTP GET", url)
        r = requests.get(url)
        json_dict = r.json()
        return json_dict
    except requests.exceptions.RequestException as error:
        print(error)


def download_json(url, filepath):
    try:
        print("HTTP GET", url)
        r = requests.get(url)
        json_dict = r.json()
        json_str = json.dumps(json_dict, indent=2, ensure_ascii=False)
        with open(filepath, "w") as f:
            f.write(json_str)
    except requests.exceptions.RequestException as error:
        print(error)


def download_csv(url, filepath):
    try:
        print("HTTP GET", url)
        r = requests.get(url)
        with open(filepath, 'w') as f:
            writer = csv.writer(f)
            for line in r.iter_lines():
                writer.writerow(line.decode('utf-8').split(','))
    except requests.exceptions.RequestException as error:
        print(error)
