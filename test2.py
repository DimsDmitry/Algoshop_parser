from time import *

import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options






def name_search(address):
    marks = driver.find_elements(by=By.ID, value='content')



link = 'http://algoshop.tilda.ws/'


stime = time()
# Initialize Firefox/Gecko WebDriver
driver = webdriver.Firefox()
firefox_options = Options()
driver = webdriver.Firefox(executable_path=".\geckodriver.exe", options=firefox_options)

try:
    driver.get(link)
    sleep(5)
    marks = driver.find_elements(by=By.XPATH, value='/html/body/div[1]/div[3]/div/div/div/div[2]/div[1]/div/div')
    for mark in marks:
        print(mark)
except:
    print('Что-то пошло не так')