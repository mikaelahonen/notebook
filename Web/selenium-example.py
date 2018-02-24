from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Remember to install browser's driver and set PATH variable
browser = webdriver.Firefox()

browser.get('http://www.yahoo.com')
assert 'Yahoo' in browser.title

elem = browser.find_element_by_name('p')  # Find the search box
elem.send_keys('text to search' + Keys.RETURN)

#Wait 3 seconds to see the typed result
time.sleep(3)

browser.quit()