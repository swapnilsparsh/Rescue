import pywhatkit as kit
import pyautogui as pg
from datetime import datetime, timedelta


def send_whatsapp(numbers, name, link):
    message = f"""🚨🛑 *Emergency* 🛑🚨
{name} is in emergency and need your help immediately.
Click the link below for location
{link}"""
    time = str(datetime.now() + timedelta(seconds=90))
    hour, minute = time[11:13], time[14:16]
    if hour[0] == "0":
        hour = hour[1]
    if minute[0] == "0":
        minute = minute[1]
    hour, minute = int(hour), int(minute)
    for x in range(len(numbers)):
        kit.sendwhatmsg(numbers[x], message, hour, minute + int(x), wait_time=20)
        pg.press("enter")
