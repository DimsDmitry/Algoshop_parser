from time import *

import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


def connect(test_link):
    responce = requests.get(test_link).text
    soup = BeautifulSoup(responce, "html.parser")
    return soup


def name_search(test_link):
    list1 = []
    block = test_link.find_all("div", class_="t-slds__caption__container")
    for elem in block:
        elem = elem.text
        list1.append(elem)
    return list1



#<div class="t-slds__title t-name t-name_xs" data-redactor-toolbar="no" style="" field="gi_title__0">Значок Алгоритмика - 30 Астрокоинов</div>


link = 'http://algoshop.tilda.ws/'


# stime = time()
# Initialize Firefox/Gecko WebDriver
# driver = webdriver.Firefox()
# firefox_options = Options()
# driver = webdriver.Firefox(executable_path=".\geckodriver.exe", options=firefox_options)

address = connect(link)
result = name_search(address)
print(result)
