import requests

res = requests.get("https://ipinfo.io/")
data = res.json()

city = data["city"]
state = data["region"]
location = data["loc"].split(",")
lat = location[0]
log = location[1]
