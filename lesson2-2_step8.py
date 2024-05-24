from selenium import webdriver
from selenium.webdriver.common.by import By
import os

url ='http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)

    inputs = browser.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
    for input in inputs:
        input.send_keys('Lorem')

    file_input = browser.find_element(By.CSS_SELECTOR, 'input[type="file"]')
    file = os.path.join(os.path.dirname(__file__), 'empty.txt')
    print(file)
    file_input.send_keys(file)

    browser.find_element(By.TAG_NAME, 'button').click()

finally:
    print(browser.switch_to.alert.text.split()[-1])
    browser.quit()


