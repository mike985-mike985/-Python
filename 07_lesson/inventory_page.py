# Каталог магазина
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_product_to_cart(self, product_name):
        # Добавляем товар в корзину по названию
        xpath = f"//div[text()='{
            product_name}']/ancestor::div[@class='inventory_item']//button"
        add_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, xpath)))
        add_button.click()

    def go_to_cart(self):
        # Переход в корзину
        cart_link = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
        cart_link.click()
