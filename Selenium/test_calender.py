from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=r'D:\drivers\chromedriver_win32\chromedriver.exe')
driver.get("http://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")
driver.maximize_window()


def click_function(variable,):
    return driver.find_element(By.XPATH,variable).send_keys('10/02/2021').click()

ele = "//input[@id = 'datepicker']"

click_function(ele)








