from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class YaMainPage:
    URL = 'https://www.ya.ru'

    BUTTON_TEXT_LOCATOR = (By.CLASS_NAME, 'button__text')
    BUTTON_LOCATOR = (By.CLASS_NAME, 'button')
    EMAIL_LINK_LOCATOR = (By.CLASS_NAME, 'b-inline')
    YANDEX_LINK_LOCATOR = (By.CLASS_NAME, 'layout__footer-logo')

    MISSPELL_LOCATOR = (By.CLASS_NAME, 'misspell__message')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def get_button_text(self):
        button = self.browser.find_element(*self.BUTTON_TEXT_LOCATOR)
        return button.text

    def get_email_link_text(self):
        link = self.browser.find_element(*self.EMAIL_LINK_LOCATOR)
        return link.text

    def press_yandex_button(self):
        link = self.browser.find_element(*self.YANDEX_LINK_LOCATOR)
        link.click()
        self.browser.implicitly_wait(2)
        return self.browser.current_url

    def press_mail_link(self):
        link = self.browser.find_element(*self.EMAIL_LINK_LOCATOR)
        link.click()
        self.browser.implicitly_wait(2)
        return self.browser.current_url

    def do_empty_search(self):
        button = self.browser.find_element(*self.BUTTON_LOCATOR)
        button.click()
        self.browser.implicitly_wait(10)
        misspell_message = self.browser.find_element(*self.MISSPELL_LOCATOR)
        return misspell_message.text
