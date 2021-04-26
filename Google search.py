# Google Search
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com") #http required

elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("Burhanuddin Petiwala") #Input your keyword to search here
elem.send_keys(Keys.RETURN)
time.sleep(8)
driver.close()