from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

url = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)

    def getNum(id):
        num = int(browser.find_element(By.ID, id).text)
        return num
    
    sum = getNum('num1') + getNum('num2')

    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_visible_text(str(sum))

    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    print(browser.switch_to.alert.text.split()[-1])
    time.sleep(5)
    browser.quit()
