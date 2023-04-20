import pytest
from selenium import webdriver
from Pages.KeyCloackAuthPage import KeyCloackAP

driver = webdriver.Chrome()
cpPage = KeyCloackAP(driver)

@pytest.fixture()
def pre_test(request):
    cpPage.load()

def teardown_module(module):
    driver.close()

def check_auth(phrase):
    #assert phrase in driver.H1, 'Url changed'
    assert phrase in driver.title

def test_chechAuthCP():
    inputName("admin@svrauto.ru").inputPass("adminPass").clickSubmit()
    check_auth('Управление опциями')