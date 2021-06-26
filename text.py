from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from arq import *

def page(link_of_page,name_page):
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options)

    URL = link_of_page

    driver.get(URL)
    time.sleep(3)
    el = driver.find_element_by_tag_name('body')
    new_text = el.text
    driver.quit()
    name_page = name_page+'.txt'
    
    #calling arq.py
    filescode(name_page,new_text,link_of_page)
    
    pass    