from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

url = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)

    x = browser.find_element(By.ID, 'treasure').get_attribute('valuex')
    calc = str(math.log(abs(12*math.sin(int(x)))))

    browser.find_element(By.ID, 'answer').send_keys(calc)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(5)
    browser.quit()