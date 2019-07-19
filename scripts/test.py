import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote,unquote
import pickle
import time
item = "Red Mango"


data = {"user": {"email": "alexanderjbusch@gmail.com", "password": "password"},
        "authenticity_token": ""}
headers = {
    'user-agent':'Mozilla/5.0',
    'x-requested-with': 'XMLHttpRequest'}
s = requests.Session()
res = s.get('https://www.instacart.com/',headers={'user-agent':'Mozilla/5.0'})
soup = BeautifulSoup(res.text, 'lxml')
token = soup.select_one("[name='csrf-token']").get('content')
data["authenticity_token"] = token
s.post("https://www.instacart.com/accounts/login",json=data,headers=headers)
json_data = s.get("https://www.instacart.com/v3/bundle?source=web&cache_key=8e26a7-22089-f-259")
print(json_data)

# write test code here
