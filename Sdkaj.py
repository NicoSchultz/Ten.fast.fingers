from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome('/Users/nicolai/PycharmProjects/helloworld/chromedriver')
driver.get("https://10fastfingers.com/typing-test/danish")
elem = driver.find_element_by_id("inputfield")
words = driver.find_element_by_id("row1").find_elements(By.TAG_NAME, 'span')
for word in words:
    #print(word.text)
    elem.send_keys(word.text + ' ')
raw_input("pressanykey")
driver.close()