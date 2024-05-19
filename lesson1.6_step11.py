from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print('Тест запущен')
try: 
    # link = "https://suninjuly.github.io/registration1.html"
    link = "https://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    fields = browser.find_elements(By.CSS_SELECTOR, '[required]')
    for field in fields:
        field.send_keys('Lorem')

    # Отправляем заполненную форму
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    control_text = "Congratulations! You have successfully registered!"
    assert  control_text == welcome_text
    print('Тест успешно пройден' if control_text == welcome_text else 'Тест провален')

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
    print('Тест окончен')
