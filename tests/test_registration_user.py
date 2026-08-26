import time
from models.user import User
from pages.registration_page import RegistrationPage


# --------Valid unique email generator------
def generate_unique_email():
    timestamp = int(time.time() * 1000)
    return f"user_{timestamp}@gmail.com"

# ----------REGISTRATION----------
#-------1. Unregistered user can register with valid data------
def test_registration_valid_data_unregister_user1(driver):
    email=generate_unique_email()
    registration_page=RegistrationPage(driver)
# -----
    user=User(
        email,
        "Weather159159!"
    )
# -----
    registration_page.open_registration_form()
    registration_page.fill_email(user.email)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()
    assert registration_page.is_registered() is True


#-------2. Unregistered user can`t register with invalid email and valid password------
def test_registration_valid_pwd_invalid_email_unregistered_user1(driver):
    registration_page = RegistrationPage(driver)
# -----
    user=User(
        "weathergmail.com",
        "Weather159159!"
    )
# -----
    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.submit_registration()
    alert_text=registration_page.get_alert_text()
    assert "Wrong email or password" in alert_text


#-------3. Unregistered user can`t register with valid email and invalid password------
def test_registration_invalid_pwd_valid_email_unregistered_user1(driver):
    email = generate_unique_email()
    registration_page = RegistrationPage(driver)
# -----
    user = User(
        email,
        "000"
    )
# -----
    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.submit_registration()
    alert_text=registration_page.get_alert_text()
    assert "Wrong email or password" in alert_text


#-------4. Registered user can`t register with registered data (email and password)------
def test_registration_registered_pwd_registered_email1(driver):
    registration_page = RegistrationPage(driver)
# -----
    user = User(
        "anna12345@gmail.com",
        "123456!Anna"
    )
# -----
    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.submit_registration()
    alert_text=registration_page.get_alert_text()
    assert "User already exist" in alert_text


#-------5. Registered user can`t register with registered email and new valid password------
def test_registration_valid_pwd_registered_email1(driver):
    registration_page = RegistrationPage(driver)
# -----
    user = User(
        "anna12345@gmail.com",
        "Weather159159!"
    )
# -----
    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.submit_registration()
    alert_text=registration_page.get_alert_text()
    assert "User already exist" in alert_text
