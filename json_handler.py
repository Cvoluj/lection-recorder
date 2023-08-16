import json
from datetime import datetime


class JSONHandler:
    def __init__(self, filename: str):
        self.filename = filename
    
    def read_file(self):
        try:
            with open(self.filename, 'r', encoding='UTF-8') as f_o:
                data_from_json = json.load(f_o)
            return data_from_json
        except FileNotFoundError:
            print("Error: File not found.")
            return {}
        except json.JSONDecodeError:
            print("Error: JSON decoding failed.")
            return {}
    
    def get_current_day(self):
        
        current_day = datetime.now().strftime('%A')
        data = self.read_file()
        try:
            day_from_json = data[current_day]
            return day_from_json
        except Exception as e:
            print(f'There no such day in calendar')
            return []

    def get_times(self):
        day = self.get_current_day()
        times = []
        for index in day:
            index = index.split('-')[0]
            times.append(index)

        return times
    
    def __call__(self):
        """
        return list with times when you need to join lecture
        """
        return self.get_times()

if __name__ == '__main__':
    json_handler = JSONHandler('calendar.json')
    print(json_handler())