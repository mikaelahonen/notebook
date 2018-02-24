from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Remember to install browser's driver and set PATH variable
browser = webdriver.Firefox()
browser.get('https://www.google.com')

#Type to search box
box = browser.find_element_by_id('lst-ib')
box.send_keys('mikaelahonen.com')

#Click search button
btn_search = browser.find_element_by_name('btnK')
btn_search.click()

#Get search results
r1 = browser.find_element_by_xpath("//h3[@class='r']/a")
r1.click()

#Find link text
contact = browser.find_element_by_link_text('Ota yhteyttä')
contact.click()

#Find form inputs and type text
input_name = browser.find_element_by_id('nf-field-17')
input_name.send_keys('John Smith')

input_email = browser.find_element_by_id('nf-field-18')
input_email.send_keys('example@example.com')

input_msg = browser.find_element_by_id('nf-field-19')
input_msg.send_keys('Hi! This is my mesage.')

#Click send button
btn_send = browser.find_element_by_id('nf-field-20')
btn_send.click()

#Wait 3 secs to see the form
time.sleep(3)

#Quit
browser.quit()