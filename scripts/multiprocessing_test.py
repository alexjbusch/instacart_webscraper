#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#import requests
import time
import os
from bs4 import BeautifulSoup
import pickle
#from requestium import Session, Keys
from multiprocessing.pool import ThreadPool

#store_name = "wegmans"
item = "horizon 1%"


price_list = []

from selenium import webdriver
from selenium.webdriver.chrome.options import Options  

chrome_options = Options()  
chrome_options.add_argument("--headless")
chrome_driver = os.getcwd() +"\\chromedriver.exe"

def scrape(store):
    #s = Session(r"C:\Users\Alex Busch\Desktop\chromedriver.exe", browser='chrome', default_timeout=15)
    #driver = s.driver
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
    driver.get("http://www.instacart.com/accounts/login.com")

    try:
        email_box = driver.find_element_by_id("login_with_password_form_email")
        email_box.send_keys("alexanderjbusch@gmail.com")
        password_box = driver.find_element_by_id("login_with_password_form_password")
        password_box.send_keys("password")
        driver.find_element_by_xpath("//button[@type='submit']").click()
    except Exception as e:
        #print(e)
        pass

    finished = False
    while not finished:
        try:
            driver.find_element_by_xpath("//a[@class='primary-nav-link']").click()
            finished = True
        except Exception as e:
            #print(e)
            pass
    finished = False
    while not finished:
        try:
            driver.find_elements_by_xpath("//button[@class='rmq-cb9cc2fa rmq-b5beda40 rmq-92e48e80']")[store].click()
            print(driver.find_elements_by_xpath("//button[@class='rmq-cb9cc2fa rmq-b5beda40 rmq-92e48e80']")[store].text.splitlines()[0])
            finished = True
        except Exception as e:
            #print(e)
            pass
    finished = False
    while not finished:
        try:
            time.sleep(1)
            driver.find_element_by_xpath("//input").send_keys("mango")
            finished = True
            
        except Exception as e:
            #print(e)
            pass

    try:
        driver.find_element_by_xpath("//button[@type='submit']").click()

    except Exception as e:
        #print(e)
        pass

    prices = []
    while prices == []:
        try:
            prices = driver.find_elements_by_xpath("//li[@class='item-card']")     
        except Exception as e:
            #print(e)
            pass

    #print(store)
    for i in prices:
        print(i.text.splitlines())
    
#ThreadPool(5).map(scrape,[0,1,2,3,4,5])
scrape(0)
#scrape(1)
#scrape(2)

