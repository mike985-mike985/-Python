from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://uitestingplayground.com/dynamicid")
button = driver.find_element(By.ID, "90924675-5bd3-1914-4f48-ef211dd4b8d8")
button.click()

sleep(50)
