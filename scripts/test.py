import json
import requests
from bs4 import BeautifulSoup
store = "giant"
baseurl = 'https://www.instacart.com/store/wegmans/search_v3/horizon%201%25'
data_url = "https://www.instacart.com/v3/containers/"+store+"/search_v3/mango?source=web&cache_key=867cda-3584-f-e68&per=20&tracking.items_per_row=2&tracking.source_url=unde7fined&tracking.autocomplete_prefix=&tracking.autocomplete_term_impression_id=&tracking.search_bar_impression_event_id=7"
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
#resp = s.get(data_url, headers=headers)
#print(resp.json())

def get_store_price(store,index):
    print(store)
    data_url = "https://www.instacart.com/v3/containers/"+store+"/search_v3/mango?source=web&cache_key=867cda-3584-f-e68&per=20&tracking.items_per_row=2&tracking.source_url=unde7fined&tracking.autocomplete_prefix=&tracking.autocomplete_term_impression_id=&tracking.search_bar_impression_event_id=7"
    resp = s.get(data_url, headers=headers)
    try:
        json_data = resp.json()['container']['modules'][index]['data']['items']
    except KeyError:
        print(resp.json())
        return       
    for i in json_data:
        print((i['name']),i['pricing']['price'])
    print("\n")

"""
get_store_price("petco",1)
get_store_price("aldi",1)
get_store_price("costco",1)
get_store_price("wegmans",2)
get_store_price("safeway",2)
get_store_price("giant",2)
get_store_price("bjs",2)
get_store_price("harris-teeter",2)
get_store_price("cvs",2)
get_store_price("shoppersfood",2)
"""
from urllib.parse import quote
print(quote("% "))
