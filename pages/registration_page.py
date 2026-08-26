from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class RegistrationPage(BasePage):
    LOGIN_NAV_LINK = (By.CSS_SELECTOR,"[href='/login']")
    EMAIL_INPUT = (By.CSS_SELECTOR,"input[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR,"input[name='password']")
    REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Registration']")
    SIGN_OUT_BUTTON = (By.XPATH,"//button[text()='Sign Out']")

    # def __init__(self,driver):
    #     self.driver=driver

    def open_registration_form(self):
        # self.driver.find_element(*self.LOGIN_NAV_LINK).click()
        self.click(self.LOGIN_NAV_LINK)

    def fill_email(self,email):
        # self.driver.find_element(*self.EMAIL_INPUT).clear()
        # self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.fill(self.EMAIL_INPUT,email)

    def fill_password(self,password):
        # self.driver.find_element(*self.PASSWORD_INPUT).clear()
        # self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.fill(self.PASSWORD_INPUT,password)

#-----------------------------------------------------------------
    def fill_registration_form(self, user):
        self.fill_email(user.email)
        self.fill_password(user.password)
# -----------------------------------------------------------------

    def submit_registration(self):
        # self.driver.find_element(*self.REGISTRATION_BUTTON).click()
        self.click(self.REGISTRATION_BUTTON)

    def is_registered(self):
        try:
            WebDriverWait(self.driver,timeout=5).until (
                EC.visibility_of_element_located(self.SIGN_OUT_BUTTON)
            )
            return True
        except TimeoutException:
            return False

    # def get_alert_text(self):
    #     alert=WebDriverWait(self.driver,timeout=15).until(
    #         EC.alert_is_present()
    #     )
    #     return alert.text
    #
    # def accept_alert(self):
    #     self.driver.switch_to.alert.accept()



