from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Edge()
wait = WebDriverWait(driver, 30)


def test_form():
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполняем форму
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    # Zip-code оставляем пустым
    driver.find_element(By.NAME, "zip-code").send_keys("")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")
    # Нажимаем кнопку Submit
    submit_button = driver.find_element(By.CSS_SELECTOR,
                                        "button[type='submit']")
    submit_button.click()

    fields_to_check = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]

    for field_name in fields_to_check:
        field = driver.find_element(By.ID, field_name).get_attribute("class")

        assert "alert-success" in field, f"Поле {field}\
                заполнено, но НЕ подсвечено зелёным!"

    assert "alert-danger" in driver.find_element(
        By.ID, "zip-code").get_attribute("class"), f"Поле zip code пустое,\
                    но НЕ подсвечено красным!"
    driver.quit()
