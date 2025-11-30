from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")
input_field = driver.find_element(By.TAG_NAME, "input")
input_field.send_keys("SkyPro")
button = driver.find_element(By.CSS_SELECTOR, 'button[class*="btn-primary"]')
button.click()

wait = WebDriverWait(driver, 30)
wait.until(
    EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, 'button[class*="btn-primary"]'), "SkyPro"
    )
)
success_message = driver.find_element(
    By.CSS_SELECTOR, 'button[class*="btn-primary"]'
)
print(success_message.text)
