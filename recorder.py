from obswebsocket import obsws, requests
from dotenv import load_dotenv
import os
import time
from datetime import datetime
import pyautogui




class Recorder():
    def __init__(self, main_directory, port, password):
        self.main_directory = main_directory
        self.prepare = 1.9
        self.port = port
        self.password = password
        self.host = 'localhost'

    def record(self, folder: str, end_time: str):
        ws = obsws(self.host, self.port, self.password)
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
                    try:
                        pyautogui.click('buttons/exit.PNG')
                        print("Leaved Zoom  meeting")
                    except Exception as e:
                        print("Don't found exit button")
                    
                else:
                    print("Failed to start recording.")
            else:
                print("Failed to set recording folder.")

        finally:
            ws.disconnect()

if __name__ == '__main__':
    recorder = Recorder(main_directory='D:/OBS/lection-recorder-bot/')
    recorder.record('test', '15:59')
