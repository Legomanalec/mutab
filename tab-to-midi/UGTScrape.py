from selenium import webdriver



driver = webdriver.Chrome('Tools/chromedriver')

driver.get('https://tabs.ultimate-guitar.com/tab/led-zeppelin/stairway-to-heaven-tabs-9488')
tab = driver.find_element("xpath", "/html/body/div[1]/div[2]/main/div[2]/article[1]/section[2]/article/section[1]")









    


