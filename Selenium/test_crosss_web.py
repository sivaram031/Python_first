from selenium import webdriver
from selenium import *
import time

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

drivers = [chrome,firefox]


for i in drivers:
    i.get('http://facebook.com\login')
    i.maximize_window()
    '''screenshot methos two types'''
    #i.save_screenshot()
    #i.get_screenshot_as_file()

