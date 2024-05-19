from selenium import webdriver
from selenium.webdriver.common.by import By
import math

url = "http://suninjuly.github.io/execute_script.html"
try:
    browser = webdriver.Chrome()
    browser.get(url)

    x = int(browser.find_element(By.ID, "input_value").text)
    result = math.log(abs(12*math.sin(x)))

    input_field = browser.find_element(By.ID, 'answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_field)

    input_field.send_keys(str(result))

    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    print(browser.switch_to.alert.text.split()[-1])
    browser.quit()
