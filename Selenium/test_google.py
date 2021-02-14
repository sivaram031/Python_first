from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://google.com")
driver.maximize_window()

lan = driver.find_elements(By.XPATH,"//div[@class='b0KoTc B4GxFc']")
print(len(lan))
print(lan)
