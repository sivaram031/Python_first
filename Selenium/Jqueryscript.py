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

def values_send(option,values):
    if not values[0]=='all':
        for i in t:
            print(i.text)
            for k in range(len(values)):
                if i.text==values[k]:
                    i.click()
                    break
    else:
        try:
            for i in option:
                i.click()

        except Exception as e:
            print(e)

values_lst =['all']
values_send(t,values_lst)


#pole




