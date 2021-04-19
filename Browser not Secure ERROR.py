#Importing required modules
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#Lines needed to be added in the code
option = Options()
option.add_experimental_option("debuggerAddress","localhost:8797")

driver = webdriver.Chrome(executable_path = "D:\API\chromedriver.exe",options=option)

driver.get('https://......')

#Continue your code.....

