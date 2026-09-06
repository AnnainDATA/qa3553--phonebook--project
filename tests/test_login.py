import time
from data.user_data import create_user, exiting_user, invalid_email_user, invalid_password_user
from pages.login_page import LoginPage


# --------Valid unique email generator
def generate_unique_email():
    timestamp = int(time.time() * 1000)
    return f"user_{timestamp}@gmail.com"


# ----------LOGIN----------
#-------1. Registered user can login with valid data------
def test_login_success(driver):
    login_page=LoginPage(driver)
    # user = create_user(username=VALID_EMAIL, password=VALID_PASSWORD)
    user = exiting_user()

    login_page.open_login_form()
    login_page.fill_email(user.username)
    login_page.fill_password(user.password)
    login_page.submit_login()
    assert login_page.is_logged() is True

#-------2. Registered user can’t login with invalid email and valid password------
def test_login_with_wrong_email(driver):
    login_page=LoginPage(driver)
    # user = create_user(username=INVALID_EMAIL, password=VALID_PASSWORD)
    user = invalid_email_user()

    login_page.open_login_form()
    login_page.fill_email(user.username)
    login_page.fill_password(user.password)
    login_page.submit_login()
    assert login_page.get_alert_text()=="Wrong email or password"
    login_page.accept_alert()

#-------3. Registered user can’t login with valid email and invalid password------
def test_login_with_wrong_password(driver):
    login_page=LoginPage(driver)
    # user = create_user(username=VALID_EMAIL, password=INVALID_PWD)
    user = invalid_password_user()

    login_page.open_login_form()
    login_page.fill_email(user.username)
    login_page.fill_password(user.password)
    login_page.submit_login()
    assert login_page.get_alert_text()=="Wrong email or password"
    login_page.accept_alert()

#-------4. Unregistered user can’t login with valid email and valid password------
def test_login_unregistered_user(driver):
    login_page=LoginPage(driver)
    user = create_user(username="marta@gmail.com", password="MMa659523$")

    login_page.open_login_form()
    login_page.fill_email(user.username)
    login_page.fill_password(user.password)
    login_page.submit_login()
    assert login_page.get_alert_text()=="Wrong email or password"
    login_page.accept_alert()

