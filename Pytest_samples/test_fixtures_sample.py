import pytest
from selenium import webdriver
from webdrivermanager import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = None
@pytest.fixture(scope='module')
def intilize_driver():
    global driver
    driver = webdriver.Chrome(executable_path=r'D:\drivers\chromedriver_win32\chromedriver.exe')
    driver.get('http://google.com')
    print('---driver setup method-----')


    yield

    print('--broswer will be close----')
    driver.implicitly_wait(5)
    driver.close()

def test_google_search(intilize_driver):
    driver.find_element(By.NAME,'q').send_keys('facebook')

def test_google_url(intilize_driver):
    assert driver.title == 'Google'

@pytest.mark.usefixtures('intilize_driver')
def test_google_title():
    print('--applyed mark.usefixtures')
    assert driver.title == 'Google'

