reminders = [
    "Drink a glass of water!",
    "Walk around for 2 minutes.",
    "Stretch your arms and neck.",
    "Rest your eyes: look 20 feet away for 20 seconds.",
    "Take 5 deep, slow breaths.",
    "Roll your ankles and wrists to restore circulation.",
    "Fix your posture: relax your shoulders and uncross your legs.",
    "Do 10 quick squats or calf raises.",
    "Refill your water bottle right now.",
    "Adjust your screen brightness to match your room lighting.",
    "Drop your shoulders away from your ears and roll them backward.",
    "Do a seated torso twist: touch your opposite knee and turn around.",
    "Squeeze your shoulder blades together for 10 seconds to open your chest.",
    "Extend your legs straight out under your desk and flex your toes.",
    "Interlace your fingers behind your back and stretch your chest open.",
    "Pull your chin straight back (chin tucks) to reverse looking down at your monitor.",
    "Look up at the ceiling and slowly look side to side to stretch your throat.",
    "Massage the base of your skull and neck with your fingers for a few seconds.",
    "Stand up and do a gentle quad stretch by pulling one heel up to your glutes.",
    "Unclench your jaw and open your mouth wide to release facial tension.",
    "Do 5 seated cat-cow stretches to release lower back stiffness.",
    "Stretch your forearms: pull your fingertips back with your opposite hand.",
    "Take a quick walk to the window or a farther water station to step away.",
    "Sanitize your desk surface, keyboard, and phone real quick.",
    "Blink rapidly 10 times to naturally lubricate dry eyes from screen staring."
    ]

import os
import sys
import time
import random
from datetime import datetime
from winotify import Notification,audio

def get_icon_path():
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, "assets", "256x256.png")

def get_msg():
    return reminders[random.randint(0, len(reminders) - 1)]

def main():
    toast = Notification(
        app_id="WakeUp", 
        title="Reminder", 
        msg=get_msg(), 
        duration="short",
        icon=get_icon_path()
    )
    toast.set_audio(audio.Default, loop=False)
    toast.show()
    
def get_time():
    now = datetime.now()
    minutes = ((now.minute // 30) + 1) * 30
    next_time = now.replace(minute=0, second=0, microsecond=0)
    if minutes == 60:
        next_time = next_time.replace(hour=now.hour + 1)
    else:
        next_time = next_time.replace(hour=now.hour, minute=minutes)
    return next_time

if __name__=="__main__":
    while True:
        next_time = get_time()
        wait_seconds = (next_time - datetime.now()).total_seconds()
        # print(f"Next reminder at {next_time.strftime('%H:%M:%S')} ({int(wait_seconds)}s away)")
        time.sleep(wait_seconds)
        main()
    

