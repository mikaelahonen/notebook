from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#Remembder to set google chrome driver to PATH

# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

#Get page content
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://www.google.com")
html = driver.page_source