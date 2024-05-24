import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

def testFunction(link: str) -> str:
    try:
        browser = webdriver.Chrome()
        browser.implicitly_wait(3)
        browser.get(link)
        # Заполняем поля
        browser.find_element(By.TAG_NAME, "input").send_keys("Ivan")
        browser.find_element(By.CLASS_NAME, "second").send_keys("Petrov")
        browser.find_element(By.CLASS_NAME, "third").send_keys("test@test.ru")
        browser.find_element(By.XPATH, "//div[@class='second_block'] //input").send_keys("88888888888")
        browser.find_element(By.XPATH, "//input[@placeholder='Input your address:']").send_keys("Samara")
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        # Сравниваем текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        return welcome_text if welcome_text else 'FAIL'
    finally:
        browser.quit()
        

control_text = "Congratulations! You have successfully registered!"

class uniqSelector(unittest.TestCase):
    def test_first(self):
        link = 'http://suninjuly.github.io/registration1.html'
        self.assertEqual(testFunction(link), control_text, f'H1 not equal to "{control_text}"')
    def test_second(self):
        link = 'http://suninjuly.github.io/registration2.html'
        self.assertEqual(testFunction(link), control_text, f'H1 not equal to "{control_text}"')

if __name__ == "__main__":
    unittest.main()