import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

loger = logging.getLogger(__name__)

class ContactsPage(BasePage):
    CONTACT_NAV_LINK = (By.CSS_SELECTOR, "[href = '/contacts']") #CONTACT BUTTON
    CONTACT_CARDS = (By.CLASS_NAME, "contact-item_card__2SOIM") #CARD
    EDIT_BUTTON = (By.XPATH,"//button[text()='Edit']")
    REMOVE_BUTTON = (By.XPATH, "//button[text()='Remove']")

    EDIT_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Name']")
    EDIT_LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Last Name']")
    EDIT_PHONE_INPUT = (By.CSS_SELECTOR, "input[placeholder='Phone']")
    EDIT_EMAIL_INPUT = (By.CSS_SELECTOR, "input[placeholder='email']")
    EDIT_ADDRESS_INPUT = (By.CSS_SELECTOR, "input[placeholder='Address']")
    EDIT_DESCRIPTION_INPUT_EDIT_CONTACT = (By.CSS_SELECTOR, "input[placeholder='desc']")
    EDIT_SAVE_BUTTON = (By.XPATH,"//button[text()='Save']")



    def open_contacts_list(self):
        self.click(self.CONTACT_NAV_LINK)
        WebDriverWait(self.driver,5).until(EC.url_contains("/contacts"))
        time.sleep(1)

    # def open_contact_card(self):
    #     self.click(self.CONTACT_CARDS)

    def open_edit_mode(self):
        loger.info("Opening edit mode")
        self.click(self.EDIT_BUTTON)

    def submit_edit(self):
        loger.info("Submitting contact edit")
        self.click(self.EDIT_SAVE_BUTTON)
        time.sleep(3)

    def set_edit_field(self,locator,value):
        self.fill(locator, value)

    #нет карточки с добавляемым номером телефона:
    def contact_card_count(self,phone):
        return len(self.driver.find_elements(By.XPATH, f"//h3[text()='{phone}']"))

    def contact_card_count1(self):
        return len(self.driver.find_elements(self.CONTACT_CARDS))

    # def open_contact_details(self,phone):
    #     card=self.driver.find_element(By.XPATH, f"//h3[text()='{phone}']/..")
    #     card.click()
    def open_contact_details(self,phone):
        loger.info(f"Opening contact details for phone{phone}")
        locator = (By.XPATH, f"//h3[text()='{phone}']/..")
        self.click(locator)


    def contact_card_visible(self,phone):
        locator = (By.XPATH, f"//h3[text()='{phone}']")
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(locator))
        return element.is_displayed()

    def get_name_value(self) -> str:
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.EDIT_NAME_INPUT)
        )
        return element.get_attribute("value") or element.text.strip()

    def contact_name_for_phone(self,phone):
        card = self.driver.find_element(By.XPATH, f"//h3[text()='{phone}']/..")
        return card.find_element(By.TAG_NAME,"h2").text

    def get_edit_contact(self,locator):
        return self.find(locator).get_attribute("value")
#----------------------------------------------------------------------
    def submit_delete(self):
        loger.info("Deleting contact")
        self.click(self.REMOVE_BUTTON)
        time.sleep(2)

    def open_first_contact(self):
        cards = self.driver.find_elements(*self.CONTACT_CARDS)
        first_card = cards[0]
        first_card.click()

    def total_contacts_count(self):
        return len(self.driver.find_elements(*self.CONTACT_CARDS))

    def remove_all_contacts(self):
        loger.info("Deleting all contacts")
        while self.total_contacts_count()>0:
            self.open_first_contact()
            self.submit_delete()