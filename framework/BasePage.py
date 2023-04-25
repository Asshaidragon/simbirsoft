import functools
import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

WAITING_TIME_FOR_AVAILABILITY = 5


def slowing_down_actions(method=None):
    @functools.wraps(method)
    def func(*args, **kwargs):
        time.sleep(1)
        return method(*args, **kwargs)

    return func


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @slowing_down_actions
    def get_element(self, locator: tuple) -> WebElement:
        return WebDriverWait(self.driver, WAITING_TIME_FOR_AVAILABILITY).until(
            expected_conditions.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    @slowing_down_actions
    def get_elements(self, locator: tuple) -> list:
        return WebDriverWait(self.driver, WAITING_TIME_FOR_AVAILABILITY).until(
            expected_conditions.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}",
        )

    @slowing_down_actions
    def go_to_url(self, url: str) -> None:
        return self.driver.get(url)

    @slowing_down_actions
    def send_keys(self, web_element: tuple, text: str) -> None:
        """Performs text input of the passed field"""
        WebDriverWait(self.driver, WAITING_TIME_FOR_AVAILABILITY).until(
            expected_conditions.element_to_be_clickable(web_element)
        ).send_keys(text)

    @slowing_down_actions
    def click(self, web_element: tuple) -> None:
        """Performs click on element"""
        WebDriverWait(self.driver, WAITING_TIME_FOR_AVAILABILITY).until(
            expected_conditions.element_to_be_clickable(web_element)
        ).click()
