# lection-recorder
Simple recorder script for recording lectures, streams etc. at current time during week
# Unrealised
This project still in developing, but now it has all main features that I wanted realise. Feel free to do same and improve it, if you interested
# Features
* Automated lecture recording based on a predefined schedule.
* Easy configuration through a JSON file.
* Support for various platforms such as YouTube, Twitch, and Zoom.
* Automaticly leave meeting (only for Zoom, but in future will be for different platforms)

# Usage

Clone this repository to your local machine:


```
git clone https://github.com/Cvoluj/lection-recorder.git
```

Create 'calendar.json'
Modify the calendar.json file to match your desired lecture schedule:

```
{
    "Monday": {
        "even_week": { // if not matter what week just paste from even_week to odd_week
            "time": ["12:25-11:40", "18:34-18:35"],
            "links": ["https://youtube.com", "https://www.twitch.tv/"],
            "subject": ["math", "test_twitch"] // It's a folder in which will be saved recording
        },
        "odd_week": {
            "time": ["10:00-11:15", "14:30-15:45"],
            "links": ["https://zoom.us", "https://google.com"],
            "subject": ["english", "history"]
        }
    },
}
```

Replace the example schedule with your own lecture days, times, links, and subjects. 
<br> **You can update calendar.json even when script started** <br>
Run the script to start recording lectures:

```
python main.py
```

# Configuration
* calendar.json: This JSON file contains the lecture schedule. Each day is associated with specific times, links, and subjects.
* main_directory: This is a parameter in **main.py** that contains basic directory for saving videos
* .env: requires such parameters as <br>
OBS_PASSWORD - stores in OBS websocket <br>
OBS_PATH - path to your obs64.exe for example C:/Program Files/obs-studio/bin/64bit/ <br> 
PORT - stores in OBS websocket
# Dependencies
* Python 3.x
* x64 version of OBS
* **IMPORTANT** - use OBS version compatible with websocket version 4.9.1
personally, I use: 
    [obs-websocket 4.9.1](https://github.com/obsproject/obs-websocket/releases/tag/4.9.1), 
    [OBS Studio 27.2.4](https://github.com/obsproject/obs-studio/releases/tag/27.2.4)

# Contributing
If you'd like to contribute to this project, feel free to create a pull request or open an issue.

# License
This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).


