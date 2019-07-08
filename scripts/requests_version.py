import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote,unquote
item = "mango"


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

def get_store_price(store):
    print(store)
    data_url = "https://www.instacart.com/v3/containers/"+store+"/search_v3/"+item+"?source=web&cache_key=867cda-3584-f-e68&per=20&tracking.items_per_row=2&tracking.source_url=unde7fined&tracking.autocomplete_prefix=&tracking.autocomplete_term_impression_id=&tracking.search_bar_impression_event_id=7"
    resp = s.get(data_url, headers=headers)
    items_found = False
    no_items_message = ""
    try:
        no_items_message = resp.json()['container']['modules'][0]['data']['description_lines'][0][:16]
    except KeyError:
        items_found = True
        
    if no_items_message == "We couldn't find" or not items_found:
        print(store+" has no items called "+unquote(item))
        return
    else:     
        try:
            json_data = resp.json()['container']['modules'][1]['data']['items']
        except KeyError:         
            try:
                json_data = resp.json()['container']['modules'][2]['data']['items']
            except Exception as e:
                json_data = resp.json()['container']['modules'][3]['data']['items']
            


    for i in json_data:
        print((i['name']),i['pricing']['price'])
    print("\n")

def get_item_prices(raw_item):
    global item
    for i in {".","/"}:
        raw_item = raw_item.replace(i,"")
    item = quote(raw_item)
    if item == "":
        print("You didn't search for anything...")
        return
    get_store_price("giant")
    get_store_price("petco")
    get_store_price("aldi")
    get_store_price("costco")
    get_store_price("wegmans")
    get_store_price("safeway")
    get_store_price("bjs")
    get_store_price("harris-teeter")
    get_store_price("cvs")
    get_store_price("shoppersfood")

usr_input = input("search for an item by typing the name of the item \n")
get_item_prices(usr_input)
