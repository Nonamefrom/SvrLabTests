from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 4)

    def click(self, webelement):
        el = self._wait.until(expected_conditions.element_to_be_clickable(webelement))
        self._highlight_element(el, "green")
        el.click()

    def fill_text(self, webelement, txt):
        el = self._wait.until(expected_conditions.element_to_be_clickable(webelement))
        el.clear()
        self._highlight_element(el, "green")
        el.send_keys(txt)

    def clear_text(self, webelement):
        el = self._wait.until(expected_conditions.element_to_be_clickable(webelement))
        el.clear()

    def _highlight_element(self, element, color):
        bg_color = element.value_of_css_property("background-color")
        self._driver.execute_script("arguments[0].style.backgroundColor = '" + color + "'", element)
        self._driver.execute_script("arguments[0].style.backgroundColor = '" + bg_color + "'", element)