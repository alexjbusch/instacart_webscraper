import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote,unquote
import pickle
import time
import sys
from seleniumwire import webdriver
from selenium.webdriver.firefox.options import Options
import re


driver = None
def login():
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    global driver
    driver = webdriver.Firefox(options=options)
    url = 'https://www.instacart.com'
    driver.get(url)
    request_cookies_browser = driver.get_cookies()
    data = {"user": {"email": "alexanderjbusch@gmail.com", "password": "password"},
            "authenticity_token": ""}
    headers = {
        'user-agent':'Mozilla/5.0',
        'x-requested-with': 'XMLHttpRequest'}
    s = requests.Session()
    c = [s.cookies.set(c['name'], c['value']) for c in request_cookies_browser]
    res = s.get('https://www.instacart.com/',headers={'user-agent':'Mozilla/5.0'})
    soup = BeautifulSoup(res.text, 'lxml')
    token = soup.select_one("[name='csrf-token']").get('content')
    data["authenticity_token"] = token
    resp = s.post("https://www.instacart.com/accounts/login",json=data,headers=headers)

    dict_resp_cookies = resp.cookies.get_dict()
    response_cookies_browser = [{'name':name, 'value':value} for name, value in dict_resp_cookies.items()]
    c = [driver.add_cookie(c) for c in response_cookies_browser]
def get_cache_key():
    login()
    driver.get('https://www.instacart.com/')
    key = None
    for request in driver.requests:
        if request.response:
            if "cache_key=" in request.path:
                potential_key = request.path.split("cache_key")[1]       
                if "undefined" not in potential_key:
                    if potential_key != "":
                        if re.search('[a-zA-Z]',potential_key) != None: 
                            key = request.path.split("cache_key=")[1]
                            driver.close()
                            driver.quit()
                            return key

def get_cart_num():
    login()
    driver.get('https://www.instacart.com/')
    driver.find_element_by_xpath("//div[@class='header-primary-nav-right']//button").click()
    key = None
    cart = None
    time.sleep(3)
    for request in driver.requests:
        if request.response:
            if "carts" in request.path:
                cart = re.search(r"carts\/(.*)\?",request.path)[1]
                key = re.search(r"cache_key=(.*)\&updated",request.path)[1]
                driver.close()
                driver.quit()
                return (cart,key)
                


print(get_cart_num())
