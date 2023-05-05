from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

options = Options()
options.page_load_strategy = "normal"
service = Service(executable_path='suchrome_driver/chromedriver')
driver = webdriver.Chrome(service=service,options=options)
str = "http://www.google.com?q=pappagallo"
driver.get(str)

titolo = driver.title

print(titolo)