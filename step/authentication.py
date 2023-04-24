from selenium.webdriver.chrome.webdriver import WebDriver

from pages.LoginPage import LoginPage, LOGIN_PAGE_URL


def log_in_as_user(driver: WebDriver, user_name: str) -> None:
    login_page = LoginPage(driver)
    login_page.go_to_url(LOGIN_PAGE_URL)
    login_page.click_on_customer_login_button()
    login_page.select_name_and_login(user_name)
