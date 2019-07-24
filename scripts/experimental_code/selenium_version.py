#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#import requests
import time
from bs4 import BeautifulSoup
import pickle
import os
from requestium import Session, Keys
from selenium.webdriver.chrome.options import Options  
from selenium import webdriver

chrome_options = Options()  
#chrome_options.add_argument("--headless")
chrome_driver = os.getcwd() +"\\chromedriver.exe"

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
driver.get("http://www.instacart.com/accounts/login.com")

def login():
    email_box = driver.find_element_by_id("login_with_password_form_email")
    email_box.send_keys("alexanderjbusch@gmail.com")
    password_box = driver.find_element_by_id("login_with_password_form_password")
    password_box.send_keys("password")
    driver.find_element_by_xpath("//button[@type='submit']").click() 

# TODO: FIX ERRORS SO I CAN ACTUALLY GET TO THE OPEN CART BUTTON
try:
    login()
except Exception as e:
    driver.find_element_by_xpath("//form//a").click()
    try:
        login()
    except:
        try:
            login()
        except:
            pass
    
time.sleep(5)
driver.find_element_by_xpath("//a[@aria-label='open cart']").click()      
"""
finished = False
while not finished:
    try:
        driver.find_element_by_xpath("//a[@class='primary-nav-link']").click()
        finished = True
    except Exception as e:
        print(e)

finished = False
while not finished:
    try:
        driver.find_elements_by_xpath("//button[@class='rmq-cb9cc2fa rmq-b5beda40 rmq-92e48e80']")[2].click()
        finished = True
    except Exception as e:
        print(e)
    
finished = False
while not finished:
    try:
        time.sleep(1)
        driver.find_element_by_xpath("//input").send_keys("mango")
        finished = True
        
    except Exception as e:
        print(e)


try:
    driver.find_element_by_xpath("//button[@type='submit']").click()

except Exception as e:
    print(e)


prices = []
while prices == []:
    try:
        prices = driver.find_elements_by_xpath("//li[@class='item-card']")     
    except Exception as e:
        print(e)

for i in prices:
    print(i.text.splitlines())
"""
