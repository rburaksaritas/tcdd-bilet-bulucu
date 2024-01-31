import json
import datetime

def load_stations():
    with open('stations.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def format_date(date):
    return datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%b %d, %Y")
