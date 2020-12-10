from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import selenium

driver = webdriver.Chrome()
driver.get('http://myvodafone.com.ws/care/register')
driver.maximize_window()


x = driver.find_element_by_id('Island')
drop = Select(x)
drop.select_by_index(1)

time.sleep(3)
l =driver.find_element_by_id('village').send_keys('v')

time.sleep(5)
n = driver.find_elements_by_xpath('//*[@id="ui-id-1"]/li')
print(len(n))

for i in n:
    t = i.text.encode('ascii','ignore').decode('ascii')
    print([t])
    if t =='Vaega':
        i.click()











