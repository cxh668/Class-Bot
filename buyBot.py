from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s = Service('C:/chromedriver_win32/chromedriver.exe')
browser = webdriver.Chrome(service=s)

browser.get('https://sis.case.edu')
browser.find_element(By.XPATH, 'userid').send_keys('cxh668')
browser.find_element(By.XPATH, 'pwd').send_keys('1090214612E45Chase12E45')
browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.RETURN)

