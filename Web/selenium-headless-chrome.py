from selenium import webdriver

#Remembder to set google chrome driver to PATH

#Some errors are produced for unknown reasib

# instantiate a chrome options object so you can set the size and headless preference
opt = webdriver.ChromeOptions()
opt.add_argument("headless")
opt.add_argument("disable-gpu")
opt.add_argument("force-enable-metrics-reporting")

#Get page content
driver = webdriver.Chrome(chrome_options = opt) #executable_path=chrome_driver
driver.get("http://google.com")
html = driver.page_source
print("Content length: " + str(len(html)))

driver.quit()