import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote,unquote
import pickle
import time
import re


#TODO: TEST REQUEST.PUT ON ZIP CODE


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
