from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get('http://spicejet.com')
driver.maximize_window()


action = ActionChains(driver)
menu = driver.find_element_by_class_name('link')

submenu = driver.find_element(By.LINK_TEXT,'LOGIN / SIGNUP')
club = driver.find_element(By.XPATH,'//a[text()="SpiceClub Members"]')


action.move_to_element(menu)
action.move_to_element(submenu)
action.perform()
action.move_to_element(club)
action.perform()


time.sleep(5)
sign= driver.find_element(By.LINK_TEXT,'Member Login')
sign.click()



