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
res = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
data = res.json()
price = data['rates']['EUR']
print(f"هر دلار برابر است با {price} یورو")