import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


driver = webdriver.Chrome(executable_path=r'D:\drivers\chromedriver_win32\chromedriver.exe')

def mytrip():
    driver.get('https://www.makemytrip.com/flights/?cmp=SEM|D|DF|G|Brand|B_M_Makemytrip_Search_Exact|Brand_Top_5_Exact|Expanded|162031058804&s_kwcid=AL!1631!3!162031058804!e!!g!!make%20my%20trip&ef_id=Cj0KCQiA0-6ABhDMARIsAFVdQv-T98gW0Dgkh8NeV-fAc5adzrn8XdpI0m0IUKA6RmRiQh2GBNvEZbwaAlWmEALw_wcB:G:s&gclid=Cj0KCQiA0-6ABhDMARIsAFVdQv-T98gW0Dgkh8NeV-fAc5adzrn8XdpI0m0IUKA6RmRiQh2GBNvEZbwaAlWmEALw_wcB')
    driver.maximize_window()

def select_destination(destination):
    driver.find_element(By.XPATH,destination).send_keys('kolkata').click()

x = "(//span[@class='lbl_input latoBold  appendBottom5'])[2]"
l = "//img[@alt='Make My Trip']"

mytrip()
driver.refresh()
select_destination(x)
