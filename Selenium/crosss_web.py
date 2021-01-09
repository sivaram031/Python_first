from selenium import webdriver

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

drivers = [chrome,firefox]

for i in drivers:
    i.get('http://facebook.com\login')