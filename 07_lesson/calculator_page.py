from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def set_delay(self, delay_value):
        # Устанавливаем значение задержки в поле #delay
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(str(delay_value))

    def click_button(self, text):
        # нажимаем кнопки
        for char in text:
            button = self.driver.find_element(
                By.XPATH, f"//span[text()='{char}']")
            button.click()

    def get_result(self):
        # Ждём и возвращаем текст результата
        wait = WebDriverWait(self.driver, 50)
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "div.screen"), "15"))
        result = self.driver.find_element(By.CSS_SELECTOR, "div.screen").text
        return result
