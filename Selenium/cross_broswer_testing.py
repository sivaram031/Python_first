from selenium import webdriver
from webdrivermanager import GeckoDriverManager
from webdrivermanager import ChromeDriverManager
import time

chrome = webdriver.Chrome(ChromeDriverManager().download_and_install())
firefox = webdriver.Firefox(executable_path='/home/sivaram/Drivers/chromedriver_linux64/geckodriver-v0.28.0-linux32/geckodriver')


def Chrome():
    driver = chrome
    driver.get('http://facebook.com\login')
def Firefox():
    driver = firefox
    driver.get('http://facebook.com\login')


Chrome()
Firefox()