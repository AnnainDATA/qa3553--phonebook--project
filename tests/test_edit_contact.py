import time
import pytest
from faker import Faker
from data.contact_data import create_contact
from pages.add_contact_page import ContactPage
from pages.contacts_page import ContactsPage
fake = Faker()
import logging
logger = logging.getLogger(__name__)

#1.Registered user can edit an existing contact after entering valid data in [NAME] field and save changes
@pytest.mark.skip (reason  = "passed, not relevant")
def test_edit_contact_name_updated(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact_steps(contact)
    new_name = fake.first_name()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_field(contacts_page.EDIT_NAME_INPUT, new_name)
    contacts_page.submit_edit()

    assert contacts_page.contact_name_for_phone(contact.phone) == new_name
#--------------------------------------------------------------------
#2.Registered user can edit an existing contact after entering valid data in [LAST NAME] field and save changes
@pytest.mark.skip (reason  = "passed, not relevant")
def test_edit_contact_last_name_updated(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact_steps(contact)
    new_last_name = fake.last_name()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_field(contacts_page.EDIT_LAST_NAME_INPUT, new_last_name)
    contacts_page.submit_edit()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    assert contacts_page.get_edit_contact(contacts_page.EDIT_LAST_NAME_INPUT) == new_last_name
#--------------------------------------------------------------------
#3.Registered user can edit an existing contact after entering valid data in [PHONE] field and save changes
#@pytest.mark.skip (reason  = "passed, not relevant")
def test_edit_contact_phone_updated(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact_steps(contact)
    new_phone = fake.unique.numerify("050#######")

    logger.debug(f"Old phone:{contact.phone}")
    logger.debug(f"New phone:{new_phone}")

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_field(contacts_page.EDIT_PHONE_INPUT, new_phone)
    contacts_page.submit_edit()

    assert contacts_page.contact_card_visible(new_phone)
    assert contacts_page.contact_card_count(contact.phone) == 0
#--------------------------------------------------------------------
#4.Registered user can edit an existing contact after entering valid data in [EMAIL] field and save changes
@pytest.mark.skip (reason  = "passed, not relevant")
def test_edit_contact_email_updated(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact_steps(contact)
    new_email = fake.unique.email()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_field(contacts_page.EDIT_EMAIL_INPUT, new_email)
    contacts_page.submit_edit()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    assert contacts_page.get_edit_contact(contacts_page.EDIT_EMAIL_INPUT) == new_email
#--------------------------------------------------------------------
#5.Registered user can edit an existing contact after entering valid data in [ADDRESS] field and save changes
@pytest.mark.skip (reason  = "passed, not relevant")
def test_edit_contact_address_updated(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact_steps(contact)
    new_address = fake.city()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_field(contacts_page.EDIT_ADDRESS_INPUT, new_address)
    contacts_page.submit_edit()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    assert contacts_page.get_edit_contact(contacts_page.EDIT_ADDRESS_INPUT) == new_address
#--------------------------------------------------------------------
#6.Registered user can edit an existing contact after entering valid data in [DESCRIPTION] field and save changes
@pytest.mark.skip(reason="BUG-130: Editing description saves literal string '[Object Undefined]'")
def test_edit_contact_description_updated(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact_steps(contact)
    new_description = fake.sentence()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_field(contacts_page.EDIT_DESCRIPTION_INPUT_EDIT_CONTACT, new_description)
    contacts_page.submit_edit()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    assert contacts_page.get_edit_contact(contacts_page.EDIT_DESCRIPTION_INPUT_EDIT_CONTACT) == new_description

#--------------------NEGATIVE-------------------------
# 1. Registered user can’t edit an existing contact with field blank or
# with incorrect data in field [NAME]
@pytest.mark.skip (reason  = "passed, not relevant")
def test_edit_contact_empty_name_negative(authenticated_driver):
    contacts_page = ContactsPage(authenticated_driver)
    contact_page = ContactPage(authenticated_driver)
    contact = create_contact()
    contact_page.create_contact_steps(contact)
    #new_name = ""

    contacts_page.open_contact_details(contact.phone)
    time.sleep(5)
    contacts_page.open_edit_mode()
    time.sleep(5)
    contacts_page.set_edit_field(contacts_page.EDIT_NAME_INPUT, "")
    contacts_page.submit_edit()

    assert contacts_page.contact_name_for_phone(contact.phone) == contact.name
#--------------------------------------------------------------------
# 2. Registered user can’t edit an existing contact with field blank or
# with incorrect data in field [LAST NAME]
@pytest.mark.skip (reason  = "passed, not relevant")
def test_edit_contact_empty_last_name_negative(authenticated_driver):
    contacts_page = ContactsPage(authenticated_driver)
    contact_page = ContactPage(authenticated_driver)
    contact = create_contact()
    contact_page.create_contact_steps(contact)
    #new_name = ""

    contacts_page.open_contact_details(contact.phone)
    time.sleep(5)
    contacts_page.open_edit_mode()
    time.sleep(5)
    contacts_page.set_edit_field(contacts_page.EDIT_LAST_NAME_INPUT, "")
    contacts_page.submit_edit()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    assert contacts_page.get_edit_contact(contacts_page.EDIT_LAST_NAME_INPUT) == contact.lastname

# --------------------------------------------------------------------
# 3. Registered user can’t edit an existing contact with field blank or with incorrect data in field [PHONE]
@pytest.mark.skip (reason  = "passed, not relevant")
def test_edit_contact_empty_phone_negative(authenticated_driver):
    contacts_page = ContactsPage(authenticated_driver)
    contact_page = ContactPage(authenticated_driver)
    contact = create_contact()
    contact_page.create_contact_steps(contact)
    #new_name = ""

    contacts_page.open_contact_details(contact.phone)
    time.sleep(5)
    contacts_page.open_edit_mode()
    time.sleep(5)
    contacts_page.set_edit_field(contacts_page.EDIT_PHONE_INPUT, "")
    contacts_page.submit_edit()

    assert contacts_page.contact_card_count(contact.phone) == 1

# --------------------------------------------------------------------
# 4. Registered user can’t edit an existing contact with field blank or with incorrect data in field [EMAIL]
#@pytest.mark.skip (reason  = "passed, not relevant")
@pytest.mark.skip (reason  = "passed, not relevant")
def test_edit_contact_empty_email_negative(authenticated_driver):
    contacts_page = ContactsPage(authenticated_driver)
    contact_page = ContactPage(authenticated_driver)
    contact = create_contact()
    contact_page.create_contact_steps(contact)
    #new_name = ""

    contacts_page.open_contact_details(contact.phone)
    time.sleep(5)
    contacts_page.open_edit_mode()
    time.sleep(5)
    contacts_page.set_edit_field(contacts_page.EDIT_EMAIL_INPUT, "")
    contacts_page.submit_edit()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    assert contacts_page.get_edit_contact(contacts_page.EDIT_EMAIL_INPUT) == contact.email


    #pytest -v tests/test_edit_contact.py
