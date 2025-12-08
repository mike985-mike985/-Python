from selenium import webdriver
from calculator_page import CalculatorPage
from selenium.webdriver.support.ui import WebDriverWait


def test_calculator_with_page_object():
    # Инициализируем драйвер (Chrome)
    driver = webdriver.Chrome()
    WebDriverWait(driver, 60)
    # Создаём объект страницы и открываем ее
    calc_page = CalculatorPage(driver)

    # Устанавливаем задержку 45 секунд
    calc_page.set_delay(45)

    # Выполняем вычисление: 7 + 8 =
    calc_page.click_button(["7", "+", "8", "="])

    # Получаем результат (уже дождавшись его появления)
    result = calc_page.get_result()

    # Проверяем, что результат равен "15"
    assert result == "15", f"Ожидалось 15, но получено: {result}"

    driver.quit()
