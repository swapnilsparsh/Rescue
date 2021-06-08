import requests
import json


def send_sms(mobile_numbers, name, link):
    url = "https://www.fast2sms.com/dev/bulk"
    message = f"""🚨🛑 *Emergency* 🛑🚨
               {name} is in emergency and need your help immediately.
               Click the link below for location
               {link}"""
    for mobile in mobile_numbers:
        params = {
            "authorization": "api_key",
            "sender_id": "FSTSMS",
            "message": message,
            "language": "english",
            "route": "p",
            "numbers": mobile,
        }
        response = requests.get(url, params=params)
        dic = response.json()  # json will give dict
        return dic.get("message", None)
