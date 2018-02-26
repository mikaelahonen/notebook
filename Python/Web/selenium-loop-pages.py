from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Remember to install browser's driver and set PATH variable
browser = webdriver.Firefox()

pages = [
	'https://www.google.fi', 
	'https://www.bing.com', 
	'https://www.yahoo.com/'
]

for page in pages:

	browser.get(page)

	#Get html source length
	html_source = browser.page_source

	#Print html string length
	length = len(html_source)	
	print(length)

browser.quit()