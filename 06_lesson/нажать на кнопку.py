from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")
button = driver.find_element(By.CSS_SELECTOR, 'button[class*="btn-primary"]')
button.click()

wait = WebDriverWait(driver, 30)
selector = "p[class*='bg-success']"
element = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, selector))
)
print(element.text)

success_message = driver.find_element(
    By.CSS_SELECTOR, 'p[class*="bg-success"]'
)
print(success_message.text)
