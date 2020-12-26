from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.cricbuzz.com/live-cricket-scorecard/31678/hbh-vs-ads-8th-match-big-bash-league-2020-21')
driver.maximize_window()


#ele = driver.find_elements(By.XPATH,"//a[text()=' Philip Salt ']//parent::div//following-sibling::div")
#print(len(ele))

ele = driver.find_elements(By.XPATH,"//div[@class='cb-col cb-col-100 cb-scrd-itms']")
print('thus are length of webelement', len(ele))
def player(value):
    for i in ele:
        n = i.text
        print(n)
        if n == 'Handscomb (c)':
            i.click()
            print('sucessfully clicked')





player(ele)






