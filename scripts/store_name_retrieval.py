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





#  THIS CODE STORES ALL OF THE STORE NAMES AND THEIR URL VERSIONS AS PAIRS IN A DICT
def create_slug_dict():
    store_slugs = {}
    index = 1
    while index < 637:
        data_url = "https://www.instacart.com/v3/retailers/"+str(index)
        index += 1
        resp = s.get(data_url,headers=headers)
        
        if resp.status_code != 200:
            if resp.status_code == 404:
                continue
            if resp.status_code == 429:
                print(index)
                time.sleep(20)
        try:
            resp = s.get(data_url,headers=headers)
            json_data = resp.json()["retailer"]
            store = json_data["name"]
            slug = json_data["slug"]
            store_slugs[store] = slug
        except Exception as e:
            print(e)



# THIS CODE PRINTS OUT ALL POSSIBLE STORES IN THE FOLLOWING POSTAL CODE

def get_stores_by_zip_code(zip_code):
    postal_code = zip_code
    data_url = "https://www.instacart.com/v3/containers/next_gen/retailers/delivery?previous_location%5Bdata%5D=21201&previous_location%5Btype%5D=postal_code&postal_code="+postal_code+"&source=mobile_web&cache_key=5e87a7-0-f-649"
    resp = s.get(data_url, headers=headers)
    for i in resp.json()["container"]["modules"][2]["data"]["retailers"]:
        print(i["name"])

get_stores_by_zip_code("21201")

