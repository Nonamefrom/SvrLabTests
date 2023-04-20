from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class KeyCloakAP:
    URL = 'https://develop-cp.dev.svrauto.ru/auth/login'
    nameBar = (By.XPATH, '//input[@name="username"]')
    passwordBar = (By.XPATH, '//input[@name="password"]')
    submitButton = (By.XPATH, '//button[@value="Submit"]')
    forgotPass = (By.XPATH, '//span[contains(text(),"Забыли пароль?")]')
    rememberMeChckBox = (By.XPATH, '//div[@name="rememberMe"]')

    def __init__(self, driver):
        self.driver = driver


    def load(self):
        self.driver.get(self.URL)
        self.wait = WebDriverWait(self.driver, 10)

    def inputName(self, name):
        self.driver.find_element(self.nameBar).send_keys(name)

    def inputPass(self, password):
        self.driver.find_element(self.passwordBar).send_keys(password)

    def pressSubmit(self):
        self.driver.find_element(self.submitButton).click()

    def pressForgot(self):
        self.driver.find_element(self.forgotPass).click()

