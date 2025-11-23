from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


service = FirefoxService(GeckoDriverManager().install())

driver = webdriver.Firefox(service=service)

driver.get("http://the-internet.herokuapp.com/login")

input_field = driver.find_element(By.ID, "username")
input_field.send_keys("tomsmith")

input_field = driver.find_element(By.ID, "password")
input_field.send_keys("SuperSecretPassword!")
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

success_message = driver.find_element(By.ID, "flash")
print(success_message.text)


driver.quit()
