from json_handler import JSONHandler
from event_scheduler import EventSchedule
from recorder import Recorder
from dotenv import load_dotenv
import os
import subprocess



load_dotenv()
host = 'localhost'
port = int(os.getenv('PORT'))
password = os.getenv('OBS_PASSWORD')
obs_path = os.getenv('OBS_PATH')

def process_exists(process_name):
    call = 'TASKLIST /FI "imagename eq %s"' % process_name
    output = subprocess.check_output(call, shell=True).decode('cp866')
    last_line = output.strip().split('\r\n')[-1]
    return last_line.lower().startswith(process_name.lower())

# go to obs directory, start obs64.exe and return to work directory
current_directory = os.getcwd()
if process_exists('obs64.exe'):
    pass
else:
    os.chdir(obs_path)
    os.startfile('obs64.exe')
    os.chdir(current_directory)


schedule = EventSchedule(JSONHandler('calendar.json'), Recorder(main_directory='D:/OBS/lection-recorder-bot/', port=port, password=password))
schedule.start()