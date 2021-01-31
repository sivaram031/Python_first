from selenium import webdriver
from selenium import *
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

drivers = [chrome,firefox]


for i in drivers:
    i.get('http://facebook.com\login')
    i.maximize_window()
    '''screenshot methos two types'''

    time.sleep(5)
    k = ActionChains(i)
    k.send_keys(Keys.ALT,Keys.TAB).perform()
    print('sucessfull move tab')
    #i.save_screenshot()
    #i.get_screenshot_as_file()


