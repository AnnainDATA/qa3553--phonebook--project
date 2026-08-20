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
#-------1. Registered user can login with valid data
# def test_login_success(driver):
#     login_page=LoginPage(driver)
#     login_page.open_login_form()
#     login_page.fill_email(VALID_EMAIL)
#     login_page.fill_password(VALID_PASSWORD)
#     login_page.submit_login()
#     assert login_page.is_logged() is True

#-------2. Registered user can’t login with invalid email and valid password
# def test_login_with_wrong_email(driver):
#     login_page=LoginPage(driver)
#     login_page.open_login_form()
#     login_page.fill_email(INVALID_EMAIL)
#     login_page.fill_password(VALID_PASSWORD)
#     login_page.submit_login()
#     assert login_page.get_alert_text()=="Wrong email or password"


# ----------REGISTRATION----------
#-------1. Unregistered user can register with valid data
def test_registration_valid_data_unregister_user(driver):
    email=generate_unique_email()

    login_page=LoginPage(driver)
    login_page.open_login_form()
    login_page.fill_email(email)
    login_page.fill_password(VALID_PASSWORD1)
    login_page.submit_registration()
    assert login_page.is_logged() is True

#-------2. Unregistered user can`t register with invalid email and valid password
def test_registration_valid_pwd_invalid_email_unregistered_user(driver):
    login_page = LoginPage(driver)
    login_page.open_login_form()
    login_page.fill_email(INVALID_EMAIL)
    login_page.fill_password(VALID_PASSWORD1)
    login_page.submit_registration()

    alert_text=login_page.get_alert_text()
    assert "Wrong email or password" in alert_text

#-------3. Unregistered user can`t register with valid email and invalid password
def test_registration_invalid_pwd_valid_email_unregistered_user(driver):
    email = generate_unique_email()
    login_page = LoginPage(driver)
    login_page.open_login_form()
    login_page.fill_email(email)
    login_page.fill_password(INVALID_PWD)
    login_page.submit_registration()

    alert_text=login_page.get_alert_text()
    assert "Wrong email or password" in alert_text

#-------4. Registered user can`t register with registered data (email and password)
def test_registration_registered_pwd_registered_email(driver):
    login_page = LoginPage(driver)
    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL)
    login_page.fill_password(VALID_PASSWORD)
    login_page.submit_registration()

    alert_text=login_page.get_alert_text()
    assert "User already exist" in alert_text

#-------5. Registered user can`t register with registered email and new valid password
def test_registration_valid_pwd_registered_email(driver):
    login_page = LoginPage(driver)
    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL)
    login_page.fill_password(VALID_PASSWORD1)
    login_page.submit_registration()

    alert_text=login_page.get_alert_text()
    assert "User already exist" in alert_text

