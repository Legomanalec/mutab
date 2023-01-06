from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of


from TabToMidi import *
import time

driver = webdriver.Chrome('Tools/chromedriver')


data_id = 0
for i in range(100): #There are only 100 pages of tabs
    url = "https://www.ultimate-guitar.com/explore?order=hitstotal_desc&page="+str(i)+"&type[]=Tabs"
    driver.get(url)

    url_list = []
    for tab in driver.find_elements("xpath", "//*[contains(@class, 'lIKMM g7KZB')]//*[contains(@class, 'aPPf7 HT3w5 lBssT')]"):
        url_list.append((tab.get_attribute("href"), tab.text))      
    print(url_list)
    for url in url_list:
        driver.get(url[0])
        tab_text = driver.find_element("xpath", "/html/body/div[1]/div[2]/main/div[2]/article[1]/section[2]/article/section[1]/div/section/code/pre")
        midiToTab(tab_text.text, url[1], data_id)
        data_id+=1










    


