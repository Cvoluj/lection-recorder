from json_handler import JSONHandler
from datetime import datetime
import time
import webbrowser
from recorder import Recorder

class EventSchedule():
    def __init__(self, json_handler: JSONHandler, recorder: Recorder):
        self.json_handler = json_handler
        self.recorder = recorder
        self.time_with_data = dict()

    def refresh_data(self):
        self.json_handler.read_file()  
        self.time_with_data = self.json_handler.get_time_with_data()

    def get_current_time(self):
        current_time = datetime.now().strftime('%H:%M')
        if current_time in self.time_with_data.keys():
            return current_time
        return None
        
    def open_link(self, data: dict):
        link = data['link']
        subject_folder = data['subject']
        end_time = data['end_time']
        
        if link is not None:
            try:
                webbrowser.open_new_tab(link)
                print(f"opened {link}")
                self.recorder.record(subject_folder, end_time)
                return True
            except Exception as e:
                print(f'link is not valid {e}')
        else: print('link is None')         

    def do_job(self):
        time_ = self.get_current_time()
        if time_ is not None:
            return self.open_link(self.time_with_data[time_])

    def start(self):
        while True:
            self.refresh_data()
            isOpened = self.do_job()
            if isOpened:
                time.sleep(60)
            else:
                time.sleep(10)

if __name__ == '__main__':
    
    extended = EventSchedule(JSONHandler('calendar.json'), Recorder(main_directory='D:/OBS/lection-recorder-bot/'))
    extended.start()