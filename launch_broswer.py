from selenium import webdriver



driver = webdriver.Chrome()
driver.get('http://facebook.com\login')

driver.find_element_by_id('email').send_keys(9704091318)
driver.find_element_by_id('pass').send_keys('sivaram1')
driver.find_element_by_id('loginbutton').click()

