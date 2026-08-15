from pages.login_page import LoginPage

VALID_EMAIL="anna12345@gmail.com"
VALID_PASSWORD="123456!Anna"

def test_login_success(driver):
    login_page=LoginPage(driver)

    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL)
    login_page.fill_password(VALID_PASSWORD)
    login_page.submit_login()
