from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://www.yahoo.com')
browser.save_screenshot('screenshot.png');
browser.quit()