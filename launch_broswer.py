

from selenium import webdriver
from webdrivermanager import ChromeDriverManager
from webdrivermanager import GeckoDriverManager

broswer = 'firefox'

if broswer =='chrome':
    driver= webdriver.Chrome(ChromeDriverManager().download_and_install())

elif broswer == 'firefox':
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().download_and_install())

else:
    print('give valid web broswer name')




driver = webdriver.Chrome()
driver.get('http://facebook.com\login')

driver.find_element_by_id('email').send_keys(9704091318)
driver.find_element_by_id('pass').send_keys('sivaram1')
driver.find_element_by_id('loginbutton').click()

