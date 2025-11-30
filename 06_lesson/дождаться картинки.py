from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
url = "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
driver.get(url)
images = WebDriverWait(driver, 90).until(
    EC.visibility_of_all_elements_located((By.TAG_NAME, "img"))
)
third_image = driver.find_element(By.XPATH, "//img[@id='award']")
src_value = third_image.get_attribute("src")
print(src_value)
