import pytest as pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from framework.webdriver_factory import get_webdriver, Driver


def pytest_addoption(parser):
    parser.addoption("--driver", action="store", default=Driver.REMOTE)


@pytest.fixture(scope="function")
def driver(pytestconfig):
    driver: WebDriver = get_webdriver(pytestconfig.getoption("driver").lower())
    yield driver

    driver.close()
    driver.quit()
