from selenium import webdriver
from selenium.webdriver.common.by import By
import math

url = 'http://suninjuly.github.io/alert_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)

    browser.find_element(By.TAG_NAME, 'button').click()

    browser.switch_to.alert.accept()

    x = int(browser.find_element(By.ID, 'input_value').text)
    calc = math.log(abs(12*math.sin(x)))
    browser.find_element(By.ID, 'answer').send_keys(str(calc))
    browser.find_element(By.TAG_NAME, 'button').click()

    print(browser.switch_to.alert.text.split()[-1])

finally:
    browser.quit()    