from  selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('http://spicejet.com')
driver.maximize_window()


add_on = driver.find_element_by_xpath('//*[@id="highlight-addons"]')
action = ActionChains(driver)

action.move_to_element(add_on).perform()
ele = driver.find_elements_by_xpath('//*[@id="header-addons"]/ul/li[*]/a')
for i in ele:
    print(i.text)



print(len(ele))





#ele =add_on.find_elements_by_xpath("//*[@href]")
#print(len(ele))






