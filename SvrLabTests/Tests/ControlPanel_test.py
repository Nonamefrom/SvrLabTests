from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def test_authorisation():
    driver = webdriver.Chrome()
    driver.get("https://develop-cp.dev.svrauto.ru/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(600)
    nameBar = driver.find_element(By.XPATH, "//input[@name='username']")
    nameBar.send_keys("admin@svrauto.ru")
    passBar = driver.find_element(By.XPATH, "//input[@name='password']")
    passBar.send_keys("adminPass")
    driver.find_element(By.XPATH, "//button[@value='Submit']").click()
    driver.implicitly_wait(600)
    main = driver.find_element(By.CSS_SELECTOR, ".text-h1").text
    assert "Управление опциями" in main
    driver.close()
