from selenium import webdriver
import time
from  selenium.webdriver import  ActionChains
from selenium.webdriver.chrome.options import Options


option = Options()
option.add_argument('window-size=1920,1080')
option.add_argument("--disable-dev-shm-usage")
option.add_argument('--headless')
option.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
option.add_argument("--no-sandbox")
option.add_argument("--disable-gpu")
option.add_experimental_option("debuggerAddress","localhost:8797")

#option.headless = True


driver = webdriver.Chrome(executable_path = "D:\API\chromedriver.exe",options=option)

action = ActionChains(driver)

driver.get('https://studio.youtube.com/video/cUyzrDHzQNI/comments/inbox?filter=%5B%7B%22name%22%3A%22ENGAGED_STATUS%22%2C%22value%22%3A%22COMMENT_CATEGORY_NOT_ENGAGED%22%7D%5D')
#driver.get('http://localhost:8797')


time.sleep(5)

for i in range(0,10):
    driver.find_element_by_id('action-menu-button').click()
    
    driver.find_element_by_xpath("//*[@class='style-scope ytcp-menu-service-item-renderer']").click()
    
    driver.find_element_by_xpath("//*[@id='confirm-button']").click()

    time.sleep(2)

    driver.refresh()

    time.sleep(5)