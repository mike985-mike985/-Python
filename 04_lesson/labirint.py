from selenium import webdriver

# Пример для Microsoft Edge
driver = webdriver.Edge()
driver.get("http://www.google.com")
print(driver.title)
driver.quit()