import time
from pages.login_page import LoginPage

VALID_EMAIL="anna12345@gmail.com"
VALID_PASSWORD="123456!Anna"

VALID_EMAIL1="anna1234544@gmail.com"
VALID_PASSWORD1="777777!Anna"

INVALID_EMAIL="anna12345gmail.com"
INVALID_PWD="!a2"

# --------Valid unique email generator
def generate_unique_email():
    timestamp = int(time.time() * 1000)
    return f"user_{timestamp}@gmail.com"


# ----------LOGIN----------
#-------1. Registered user can login with valid data------
def test_login_success(driver):
    login_page=LoginPage(driver)
    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL)
    login_page.fill_password(VALID_PASSWORD)
    login_page.submit_login()
    assert login_page.is_logged() is True

#-------2. Registered user can’t login with invalid email and valid password------
def test_login_with_wrong_email(driver):
    login_page=LoginPage(driver)
    login_page.open_login_form()
    login_page.fill_email(INVALID_EMAIL)
    login_page.fill_password(VALID_PASSWORD)
    login_page.submit_login()
    assert login_page.get_alert_text()=="Wrong email or password"



