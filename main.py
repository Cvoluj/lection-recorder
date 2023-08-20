from json_handler import JSONHandler
import schedule
from datetime import time, datetime, timedelta
import time

json_handler = JSONHandler('calendar.json')
times, links = json_handler()


def job(link):
    print('Succes')
    print(f'opened {link}')

def check_time(times, links):
    if datetime.now().strftime('%H:%M') in times:
        print(f'{datetime.now().strftime("%H:%M")} now')

while True:
    check_time(times, links)
    # print(datetime.now().strftime("%H:%M"))
    time.sleep(2)