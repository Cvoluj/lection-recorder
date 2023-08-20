from json_handler import JSONHandler
import schedule
from datetime import time, datetime, timedelta
import time

json_handler = JSONHandler('calendar.json')
raw_times, raw_links = json_handler()

time_with_link = dict()
for time_, link in zip(raw_times, raw_links):
    time_with_link[time_] = link
print(time_with_link)

def job(link):
    print('Succes')
    print(f'opened {link}')

def check_time(times: dict):
    if datetime.now().strftime('%H:%M') in times.keys():
        job(times[datetime.now().strftime('%H:%M')])

while True:
    check_time(time_with_link)
    # print(datetime.now().strftime("%H:%M"))
    time.sleep(2)