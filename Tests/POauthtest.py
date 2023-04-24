import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.KeyCloackAuthPage import KeyCloackAP

driver = webdriver.Chrome()
cpPage = KeyCloackAP(driver)

@pytest.fixture()
def pre_test(request):
    cpPage.load()

def teardown_module(module):
    driver.close()

def check_auth(phrase):
    assert phrase in driver.title

def load_page(phrase):
    main = driver.find_element(By.XPATH, "//span[@class='text-h1']").text
    assert phrase in main
#Тест проверки авторизации check_auth и загрузки заголовка H1 - load_page1
def test_chechAuthCP(pre_test):
    cpPage.inputName("admin@svrauto.ru").inputPass("adminPass").clickSubmit()
    check_auth('Панель управления')
    driver.implicitly_wait(600)
    load_page('Управление опциями')
