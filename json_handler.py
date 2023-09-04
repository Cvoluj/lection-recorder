import json
from datetime import datetime


class JSONHandler:
    def __init__(self, filename: str):
        self.filename = filename
        self.data_from_json = {}
    
    def read_file(self):
        try:
            with open(self.filename, 'r', encoding='UTF-8') as f_o:
                self.data_from_json = json.load(f_o)
        except FileNotFoundError:
            print("Error: File not found.")
        except json.JSONDecodeError:
            print("Error: JSON decoding failed.")
 
    def refresh_data(self):
        self.read_file()

    def get_current_week(self) -> str:
        current_week = int(datetime.now().strftime('%U'))
        if current_week % 2 == 0:
            return 'even_week'
        else:
            return 'odd_week'

    def get_current_day(self) -> dict:
        self.read_file()
        data = self.data_from_json
        
        current_day = datetime.now().strftime('%A')
        current_week = self.get_current_week()
        
        try:
            day_from_json = data[current_day][current_week]
            return day_from_json
        except Exception as e:
            print(f'There no such day in calendar')
            return []
    
    def get_times(self, index_=0) -> list:
        result = []
        for time in self.get_current_day()['time']:
            time = time.split('-')[index_]
            result.append(time)
        return result

    def get_links(self) -> list: 
        return self.get_current_day()['links']
    
    def get_subjects(self) -> list:
        return self.get_current_day()['subject']
    
    def get_end_time(self):
        return self.get_times(index_=1)
        

    def get_time_with_data(self) -> dict:
        """
        return dictionary as {time: link} 
        """
        time_with_data = dict()
        for time_, link, end_time, subject in zip(self.get_times(), self.get_links(), self.get_end_time(), self.get_subjects()):
            time_with_data[time_] = {'link': link, 
                                     'end_time': end_time, 
                                     'subject': subject}
        return time_with_data

    def __call__(self):
        """
        return times and links to join lecture
        """
        return self.get_times(), self.get_links()

if __name__ == '__main__':
    json_handler = JSONHandler('calendar.json')
    times, links = json_handler()
    time_with_links = json_handler.get_time_with_data()
    print(times)
    print(links)
    subject = json_handler.get_subjects()
    print(subject)
    print(json_handler.get_end_time())
    # print(json_handler.get_current_day())
    # print(json_handler.read_file())