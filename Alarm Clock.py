import datetime
import time
from playsound import playsound

def alarm_clock(set_time, sound_file):
    print(f"Alarm set for {set_time} ⏰")
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == set_time:
            print("Wake up! 🔔")
            playsound(sound_file)
            break
        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Set alarm time (HH:MM, 24-hour format): ")
    alarm_clock(alarm_time, "alarm.mp3")
