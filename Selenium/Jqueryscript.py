from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get('https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree')
driver.maximize_window()

s = driver.find_element_by_xpath("//input[@placeholder='Select']").click()
#sle = Select(s)

time.sleep(5)

t = driver.find_elements_by_xpath(("//span[contains(@class,'combo')]"))
print(len(t))

for i in t:
    m =i.text.encode('ascii','ignore').decode('ascii')
    if m == 'choice 5':
        i.click()




