import math
import random
import datetime as dt
import os
import requests
import json

print(math.sqrt(25))
print(random.randint(1,10))
print(dt.datetime.now())
print(os.getcwd())
response = requests.get("https://api.github.com")
print(response.status_code)
res = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
print(res.status_code)