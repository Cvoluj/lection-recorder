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
    
    def get_current_day(self) -> dict:
        
        current_day = datetime.now().strftime('%A')
        data = self.read_file()
        try:
            day_from_json = data[current_day]
            return day_from_json
        except Exception as e:
            print(f'There no such day in calendar')
            return []
    
    def get_times(self) -> list:
        result = []
        for index in self.get_current_day()['time']:
            index = index.split('-')[0]
            result.append(index)
        return result

    
    def get_links(self) -> list: 
        return self.get_current_day()['links']

    def __call__(self):
        """
        return times and links to join lecture
        """
        return self.get_times(), self.get_links()

if __name__ == '__main__':
    json_handler = JSONHandler('calendar.json')
    times, links = json_handler()
    print(times)
    print(links)
    # print(json_handler.get_current_day())
    # print(json_handler.read_file())