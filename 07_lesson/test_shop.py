from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


def test_shop():
    driver = webdriver.Chrome()
    WebDriverWait(driver, 60)

    # Создаём экземпляры страниц
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # 1. Открываем сайт и логинимся
    login_page.login("standard_user", "secret_sauce")

    # 2. Добавляем товары в корзину
    products = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    for product in products:
        inventory_page.add_product_to_cart(product)

    # 3. Переходим в корзину
    inventory_page.go_to_cart()

    # 4. Нажимаем Checkout
    cart_page.click_checkout()

    # 5. Заполняем форму
    checkout_page.fill_form("Вася", "Слон", "123456")

    # 6. Получаем итоговую сумму
    total = checkout_page.get_total_amount()

    # 7. Проверяем, что итог равен $58.29
    assert total == 58.29, f"Ожидалось $58.29, но получено: ${total}"

    driver.quit()
