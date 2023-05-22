from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Pages.BasePage import BasePage

class KeyCloackAP(BasePage):
    URL = 'https://develop-cp.dev.svrauto.ru/auth/login'
    nameBar = (By.XPATH, '//input[@name="username"]')
    passwordBar = (By.XPATH, '//input[@name="password"]')
    submitButton = (By.XPATH, '//button[@value="Submit"]')
    forgotPass = (By.XPATH, '//span[contains(text(),"Забыли пароль?")]')
    rememberMeChckBox = (By.XPATH, '//div[@name="rememberMe"]')

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        self._driver.get(self.URL)
        self.wait = WebDriverWait(self._driver, 10)

    def login(self, username, password):
        self.fill_text(self.nameBar, username)
        self.fill_text(self.passwordBar, password)
        self.click(self.submitButton)