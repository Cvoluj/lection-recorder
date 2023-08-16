import json
from datetime import datetime

def get_current_day():
    with open('calendar.json', 'r', encoding='UTF-8') as f_o:
        data_from_json = json.load(f_o)
        current_day = datetime.now().strftime('%A')
        day_from_json = data_from_json[current_day]
        return day_from_json

data_from_json = get_current_day()
print(data_from_json)
print(type(data_from_json))

def get_join_time(data: list):
    times = []
    for index in data:
        index = index.split('-')[0]
        times.append(index)

    return times
times = get_join_time(data_from_json)
print(times)