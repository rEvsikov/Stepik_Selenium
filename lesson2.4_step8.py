from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

url = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)

    button = browser.find_element(By.ID, 'book')
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element([By.ID, 'price'], '$100'))
    button.click()

    # Математика
    x = int(browser.find_element(By.ID, 'input_value').text)
    calc = math.log(abs(12*math.sin(x)))
    browser.find_element(By.ID, 'answer').send_keys(str(calc))
    browser.find_element(By.ID, 'solve').click()

    print(browser.switch_to.alert.text.split()[-1])

finally:
    browser.quit()