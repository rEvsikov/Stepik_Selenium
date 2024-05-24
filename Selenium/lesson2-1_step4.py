from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

url = 'https://suninjuly.github.io/math.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)

    x = int(browser.find_element(By.ID, 'input_value').text)
    answer = str(math.log(abs(12*math.sin(int(x)))))

    input_field = browser.find_element(By.ID, 'answer')
    input_field.send_keys(answer)

    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(5)
    browser.quit()