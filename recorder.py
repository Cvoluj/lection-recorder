from obswebsocket import obsws, requests
from dotenv import load_dotenv
import os
import time
from datetime import datetime

load_dotenv()
host = 'localhost'
port = int(os.getenv('PORT'))
password = os.getenv('OBS_PASSWORD')


class Recorder():
    def __init__(self, main_directory):
        self.main_directory = main_directory
        self.prepare = 1.9

    def record(self, folder: str, end_time: str):
        ws = obsws(host, port, password)
        ws.connect()

        try:
            if ws.call(requests.SetRecordingFolder(f'{self.main_directory}{folder}')).status:
                print(ws.call(requests.GetRecordingFolder()))
                if ws.call(requests.StartRecording()).status:
                    print("Recording started.")
                    time.sleep(self.prepare)
                    
                    end_time = datetime.strptime(end_time, '%H:%M').time()  

                    while datetime.now().time() <= end_time:
                        time.sleep(3)  # Check every second
                    ws.call(requests.StopRecording())
                    print("Recording stopped.")
                else:
                    print("Failed to start recording.")
            else:
                print("Failed to set recording folder.")

        finally:
            ws.disconnect()

if __name__ == '__main__':
    recorder = Recorder(main_directory='D:/OBS/lection-recorder-bot/')
    recorder.record('test', '13:06')
