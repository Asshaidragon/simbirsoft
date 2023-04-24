from selenium import webdriver
from selenium.webdriver import Chrome, Remote
from selenium.webdriver.chrome.service import Service


class Driver:
    LOCAL = "local"
    REMOTE = "remote"


def get_webdriver(driver_type: str) -> Chrome | Remote:
    if driver_type == Driver.LOCAL:
        return Chrome(service=Service("/usr/local/bin/chromedriver"))
    elif driver_type == Driver.REMOTE:
        return Remote(
            command_executor="http://localhost:4444",
            options=webdriver.ChromeOptions(),
        )
    else:
        raise AssertionError(
            f"The driver type is not specified. Expected: {Driver.LOCAL} or {Driver.REMOTE}"
        )
