import logging
import time
import pytest
from paramiko.agent import value

from data.contact_data import create_contact
#from models.contact import Contact
from pages.add_contact_page import ContactPage
from faker import Faker
from pages.contacts_page import ContactsPage

fake=Faker()
logger = logging.getLogger(__name__)

@pytest.mark.parametrize(
    "description",
    [
        pytest.param(None,id="all_fields"),
        pytest.param("",id="required_fields_only")
    ]
)

#------Successfully creating new contact with valid data------
#-------------------------------------------------------------
def test_add_contact_success_all_field(authenticated_driver,description):
    logger.info("Test: test_add_contact_success_all_field")
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)
    contact = create_contact() if description is None else create_contact(description=description)

    # randon_suffix = random.randint(1,10000000)
    # contact=Contact(
    #     name = fake.first_name(),
    #     lastname = fake.last_name(),
    #     phone = fake.numerify("05##########"),
    #     email = f"anna_test_{randon_suffix}@gmail.com",
    #     address = fake.city(),
    #     description = fake.text())
    contact_page.create_contact_steps(contact)
    # contact_page.open_contacts_form()
    # contact_page.fill_contact_form(contact)
    # contact_page.submit_contact()
    assert contacts_page.contact_card_visible(contact.phone)

#-------------------------------------------------------------------
def test_add_contact_success_required_field(authenticated_driver):
    logger.info("Test: test_add_contact_success_required_field")
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)
    contact = create_contact(description="")

    # randon_suffix = random.randint(1,10000000)
    # contact=Contact(
    #     fake.first_name(),
    #     fake.last_name(),
    #     f"05012{randon_suffix}",
    #     f"anna_test_{randon_suffix}@gmail.com",
    #     fake.city(),
    #     "")

    contact_page.create_contact_steps(contact)
    assert contacts_page.contact_card_visible(contact.phone)

#------Unsuccessfully creating new contact with invalid data------
#-----------------------------------------------------------------
#1.Registered user can’t create new contact with field blank or with incorrect data in field NAME-FAILED
def test_add_contact_not_success_field_name_blank(authenticated_driver):
    logger.info("Test: test_add_contact_not_success_field_name_blank")
    contact_page=ContactPage(authenticated_driver)
    contact = create_contact(name="")

    # randon_suffix = random.randint(1, 10000000)
    # contact=Contact(
    #     "",
    #     fake.last_name(),
    #     f"054{randon_suffix}",
    #     fake.unique.email(),
    #     fake.city(),
    #     fake.text())

    contact_page.create_contact_steps(contact)
    time.sleep(5)

#If the [ADD] tab stays active, the contact wasn't created and we didn't switch to the [CONTACTS] tab
    alert_text=contact_page.get_alert_text()
    assert "Name cannot be empty!" in alert_text
    contact_page.accept_alert()
    assert contact_page.is_add_tab_active()

    # contact_page.open_contacts_list()
    # assert contact_page.contact_card_count(contact.phone) == 0

#-----------------------------------------------------------------
#2.Registered user can’t create new contact with field blank or with incorrect data in field LAST NAME-FAILED
def test_add_contact_not_success_field_lastname_blank(authenticated_driver):
    contact_page=ContactPage(authenticated_driver)
    contact = create_contact(lastname="")
    contact_page.create_contact_steps(contact)
    time.sleep(5)

    alert_text=contact_page.get_alert_text()
    assert "Last Name cannot be empty!" in alert_text
    contact_page.accept_alert()
    #assert contact_page.is_contacts_tab_active()
    assert contact_page.is_add_tab_active()

#-----------------------------------------------------------------
#3.Registered user can’t create new contact with field blank or with incorrect data in field PHONE-PASSED
def test_add_contact_not_success_field_phone_blank(authenticated_driver):
    contact_page=ContactPage(authenticated_driver)
    contact = create_contact(phone="")
    contact_page.create_contact_steps(contact)
    time.sleep(5)

    alert_text=contact_page.get_alert_text()
    assert "Phone not valid: Phone number must contain only digits! And length min 10, max 15!" in alert_text
    contact_page.accept_alert()
    #assert contact_page.is_contacts_tab_active()
    assert contact_page.is_add_tab_active()
#-----
@pytest.mark.parametrize("field, value,expected_alert",INVALID_CONTACT_FIELDS)
def test_add_contact_not_success_field_phone_wrong(authenticated_driver,field, value,expected_alert):
    contact_page=ContactPage(authenticated_driver)
    contacts_page=ContactsPage(authenticated_driver)
    contact = create_contact(phone=phone)
    contact_page.create_contact_steps(contact)
    time.sleep(5)

    alert_text=contact_page.get_alert_text()
    assert "Phone not valid: Phone number must contain only digits! And length min 10, max 15!" in alert_text
    contact_page.accept_alert()
    #assert contact_page.is_contacts_tab_active()
    assert contact_page.is_add_tab_active()
#-----
def test_add_contact_not_success_field_phone_wrong_intel007(authenticated_driver):
    contact_page=ContactPage(authenticated_driver)
    contact = create_contact(phone="intel007")
    contact_page.create_contact_steps(contact)
    time.sleep(5)

    alert_text=contact_page.get_alert_text()
    assert "Phone not valid: Phone number must contain only digits! And length min 10, max 15!" in alert_text
    contact_page.accept_alert()
    #assert contact_page.is_contacts_tab_active()
    assert contact_page.is_add_tab_active()
#-----
def test_add_contact_not_success_field_phone_wrong_05405405405405488997700(authenticated_driver):
    contact_page=ContactPage(authenticated_driver)
    contact = create_contact(phone="05405405405405488997700")
    contact_page.create_contact_steps(contact)
    time.sleep(5)

    alert_text=contact_page.get_alert_text()
    assert "Phone not valid: Phone number must contain only digits! And length min 10, max 15!" in alert_text
    contact_page.accept_alert()
    #assert contact_page.is_contacts_tab_active()
    assert contact_page.is_add_tab_active()
#-----
def test_add_contact_not_success_field_phone_not_unique(authenticated_driver):
    contact_page=ContactPage(authenticated_driver)
    contact = create_contact(phone="0545699350")
    contact_page.create_contact_steps(contact)
    time.sleep(5)

    alert_text=contact_page.get_alert_text()
    assert "Phone already exists" in alert_text
    contact_page.accept_alert()
    #assert contact_page.is_contacts_tab_active()
    assert contact_page.is_add_tab_active()

#-----------------------------------------------------------------
#4.Registered user can’t create new contact with field blank or with incorrect data in field EMAIL-FAILED
#@pytest.mark.skip(reason = "BUG-123:Contact with empty mail") # - ожидаемая ошибка тест не запускается на выполнение
#@pytest.mark.xfail(reason = "BUG-123:Contact with empty mail") #- ожидаемая ошибка но тест прогоняется
def test_add_contact_not_success_field_email_blank(authenticated_driver):
    contact_page=ContactPage(authenticated_driver)
    contact = create_contact(email="")
    contact_page.create_contact_steps(contact)
    time.sleep(5)

    alert_text=contact_page.get_alert_text()
    assert "Email not valid: must have format email!" in alert_text
    contact_page.accept_alert()
    #assert contact_page.is_contacts_tab_active()
    assert contact_page.is_add_tab_active()
#------
@pytest.mark.parametrize(
"field,value,expected_alert",
[
    ("email","hgfsjdfgshdfgksjdf",EMAIL_ALERT_TEXT),
    ("email","invalid_email_format",EMAIL_ALERT_TEXT),
    ("email","עדכעכדעדע",EMAIL_ALERT_TEXT),

],
ids = ["phone_letters","invalid_email_format","hebrew","dot_after_at"])


def test_add_contact_not_success_field_email_wrong_rus_letters(authenticated_driver,field,value,expected_alert):
    contact_page=ContactPage(authenticated_driver)
    contact = create_contact(**{field:value})
    contact_page.create_contact_steps(contact)
    time.sleep(5)

    alert_text=contact_page.get_alert_text()
    assert "Email not valid: must have format email!" in alert_text
    contact_page.accept_alert()
    #assert contact_page.is_contacts_tab_active()
    assert contact_page.is_add_tab_active()
#------
def test_add_contact_not_success_field_email_wrong_without_at(authenticated_driver):
    contact_page=ContactPage(authenticated_driver)
    contact = create_contact(email="telrangmail.com")
    contact_page.create_contact_steps(contact)
    time.sleep(5)

    alert_text=contact_page.get_alert_text()
    assert "Email not valid:" in alert_text
    contact_page.accept_alert()
    #assert contact_page.is_contacts_tab_active()
    assert contact_page.is_add_tab_active()
#------
def test_add_contact_not_success_field_email_wrong_without_dot_com(authenticated_driver):
    contact_page=ContactPage(authenticated_driver)
    contact = create_contact(email="telran@gmail")
    contact_page.create_contact_steps(contact)
    time.sleep(5)

    alert_text=contact_page.get_alert_text()
    assert "Email not valid:" in alert_text
    contact_page.accept_alert()
    #assert contact_page.is_contacts_tab_active()
    assert contact_page.is_add_tab_active()
#------
def test_add_contact_not_success_field_email_not_unique(authenticated_driver):
    contact_page=ContactPage(authenticated_driver)
    contact = create_contact(email="go@tel-ran.com")
    contact_page.create_contact_steps(contact)
    time.sleep(5)

    alert_text=contact_page.get_alert_text()
    assert "Email already exists" in alert_text
    contact_page.accept_alert()
    #assert contact_page.is_contacts_tab_active()
    assert contact_page.is_add_tab_active()

#-----------------------------------------------------------------
#5.Registered user can’t create new contact with field blank or with incorrect data in field ADDRESS-FAILED
def test_add_contact_not_success_field_address_blank(authenticated_driver):
    contact_page=ContactPage(authenticated_driver)
    contact = create_contact(address="")
    contact_page.create_contact_steps(contact)
    time.sleep(5)

    alert_text=contact_page.get_alert_text()
    assert "Address cannot be empty!" in alert_text
    contact_page.accept_alert()
    assert contact_page.is_add_tab_active()

    #assert contact_page.is_contacts_tab_active()
#---------------------------------------------------------------------
#@pytest.mark.xfail(reason = "BUG-124: Duplicate phone")
def test_add_contact_duplicate_phone(authenticated_driver):
    contact_page=ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)
    shared_phone=fake.unique.numerify("050##########")
    first_contact = create_contact(phone=shared_phone)
    second_contact = create_contact(phone=shared_phone)

    contact_page.create_contact_steps(first_contact)
    time.sleep(5)
    assert contacts_page.contact_card_visible(shared_phone)

    contact_page.create_contact_steps(second_contact)
    time.sleep(5)
    contacts_page.open_contacts_list()
    assert contacts_page.contact_card_count(shared_phone) == 1


    '''
    pytest -v tests/test_add_contact.py

The purpose of the test was to sequentially enter invalid data or leave mandatory fields blank
to verify that appropriate error messages are displayed. Tests that successfully triggered 
an error message - passed, while scenarios where no error appeared - failed and required a bug report.
------------------
********** Verify that an alert message is displayed when filling in fields with an invalid date:
    
alert_text=contact_page.get_alert_text()
assert "Address cannot be empty!" in alert_text
    
collected 15 items                                                                                                                                           

tests/test_add_contact.py::test_add_contact_success_all_field PASSED                                                                                   [  6%]
tests/test_add_contact.py::test_add_contact_success_required_field PASSED                                                                              [ 13%]
tests/test_add_contact.py::test_add_contact_not_success_field_name_blank FAILED  -V                                                                    [ 20%]
tests/test_add_contact.py::test_add_contact_not_success_field_lastname_blank FAILED  -V                                                                [ 26%]
tests/test_add_contact.py::test_add_contact_not_success_field_phone_blank PASSED                                                                       [ 33%]
tests/test_add_contact.py::test_add_contact_not_success_field_phone_wrong_000000000 PASSED                                                             [ 40%]
tests/test_add_contact.py::test_add_contact_not_success_field_phone_wrong_intel007 PASSED                                                              [ 46%]
tests/test_add_contact.py::test_add_contact_not_success_field_phone_wrong_05405405405405488997700 PASSED                                               [ 53%]
tests/test_add_contact.py::test_add_contact_not_success_field_phone_not_unique FAILED  -V                                                              [ 60%]
tests/test_add_contact.py::test_add_contact_not_success_field_email_blank FAILED  -V                                                                   [ 66%]
tests/test_add_contact.py::test_add_contact_not_success_field_email_wrong_rus_letters FAILED  -V                                                       [ 73%]
tests/test_add_contact.py::test_add_contact_not_success_field_email_wrong_without_AT PASSED                                                            [ 80%]
tests/test_add_contact.py::test_add_contact_not_success_field_email_wrong_without_dot_com FAILED  -V                                                   [ 86%]
tests/test_add_contact.py::test_add_contact_not_success_field_email_not_unique FAILED  -V                                                              [ 93%]
tests/test_add_contact.py::test_add_contact_not_success_field_address_blank FAILED  -V                                                                 [100%]
========================================================== 8 failed, 7 passed in 270.69s (0:04:30) ==========================================================
********** Checking that we remain on the contact creation page, which indicates that the contact was not created:

assert contact_page.is_add_tab_active() (without assept_alert!!!)

collected 15 items                                                                                                                                                                                                                 

tests/test_add_contact.py::test_add_contact_success_all_field PASSED                                                                                                                                                         [  6%]
tests/test_add_contact.py::test_add_contact_success_required_field PASSED                                                                                                                                                    [ 13%]
tests/test_add_contact.py::test_add_contact_not_success_field_name_blank PASSED                                                                                                                                              [ 20%]
tests/test_add_contact.py::test_add_contact_not_success_field_lastname_blank PASSED                                                                                                                                          [ 26%]
tests/test_add_contact.py::test_add_contact_not_success_field_phone_blank FAILED  -V                                                                                                                                         [ 33%]
tests/test_add_contact.py::test_add_contact_not_success_field_phone_wrong_000000000 FAILED  -V                                                                                                                               [ 40%]
tests/test_add_contact.py::test_add_contact_not_success_field_phone_wrong_intel007 FAILED  -V                                                                                                                                [ 46%]
tests/test_add_contact.py::test_add_contact_not_success_field_phone_wrong_05405405405405488997700 FAILED  -V                                                                                                                 [ 53%]
tests/test_add_contact.py::test_add_contact_not_success_field_phone_not_unique FAILED  -V                                                                                                                                    [ 60%]
tests/test_add_contact.py::test_add_contact_not_success_field_email_blank FAILED  -V                                                                                                                                         [ 66%]
tests/test_add_contact.py::test_add_contact_not_success_field_email_wrong_rus_letters FAILED  -V                                                                                                                             [ 73%]
tests/test_add_contact.py::test_add_contact_not_success_field_email_wrong_without_at FAILED  -V                                                                                                                              [ 80%]
tests/test_add_contact.py::test_add_contact_not_success_field_email_wrong_without_dot_com FAILED  -V                                                                                                                         [ 86%]
tests/test_add_contact.py::test_add_contact_not_success_field_email_not_unique FAILED  -V                                                                                                                                    [ 93%]
tests/test_add_contact.py::test_add_contact_not_success_field_address_blank PASSED                                                                                                                                           [100%]
============================================================================================ 10 failed, 5 passed in 236.02s (0:03:56) =============================================================================================  
********** Verifying that we are redirected to the contacts page, which indicates that the contact was successfully created:
    
assert contact_page.is_contacts_tab_active()
    
collected 15 items                                                                                                                                                                                                                 

tests/test_add_contact.py::test_add_contact_success_all_field PASSED                                                                                                                                                         [  6%]
tests/test_add_contact.py::test_add_contact_success_required_field PASSED                                                                                                                                                    [ 13%]
tests/test_add_contact.py::test_add_contact_not_success_field_name_blank FAILED                                                                                                                                              [ 20%]
tests/test_add_contact.py::test_add_contact_not_success_field_lastname_blank FAILED                                                                                                                                          [ 26%]
tests/test_add_contact.py::test_add_contact_not_success_field_phone_blank FAILED                                                                                                                                             [ 33%]
tests/test_add_contact.py::test_add_contact_not_success_field_phone_wrong_000000000 FAILED                                                                                                                                   [ 40%]
tests/test_add_contact.py::test_add_contact_not_success_field_phone_wrong_intel007 FAILED                                                                                                                                    [ 46%]
tests/test_add_contact.py::test_add_contact_not_success_field_phone_wrong_05405405405405488997700 FAILED                                                                                                                     [ 53%]
tests/test_add_contact.py::test_add_contact_not_success_field_phone_not_unique PASSED    -V                                                                                                                                  [ 60%]
tests/test_add_contact.py::test_add_contact_not_success_field_email_blank PASSED    -V                                                                                                                                       [ 66%]
tests/test_add_contact.py::test_add_contact_not_success_field_email_wrong_rus_letters PASSED    -V                                                                                                                           [ 73%]
tests/test_add_contact.py::test_add_contact_not_success_field_email_wrong_without_at FAILED                                                                                                                                  [ 80%]
tests/test_add_contact.py::test_add_contact_not_success_field_email_wrong_without_dot_com PASSED    -V                                                                                                                       [ 86%]
tests/test_add_contact.py::test_add_contact_not_success_field_email_not_unique PASSED    -V                                                                                                                                  [ 93%]
tests/test_add_contact.py::test_add_contact_not_success_field_address_blank FAILED                                                                                                                                           [100%]

============================================================================================= 8 failed, 7 passed in 182.74s (0:03:02) =============================================================================================  
#     '''
# def test_add_contact_invalid_phone_too_short(authenticated_driver):
#     contact_page = ContactPage(authenticated_driver)
#     contacts_page = ContactsPage(authenticated_driver)
#     contact = create_contact(phone="0504")
#
#     contact_page.create_contact_steps(contact)
#
#
#     assert contact_page.get_alert_text().strip() == PHONE_ALERT_TEXT
#     contact_page.accept_alert()
#     assert contact_page.is_add_button_active()
#
#     contacts_page.open_contacts_list()
#     assert contacts_page.contact_cards_count(contact.phone) == 0
#
# def test_add_contact_invalid_phone_too_long(authenticated_driver):
#     contact_page = ContactPage(authenticated_driver)
#     contacts_page = ContactsPage(authenticated_driver)
#     contact = create_contact(phone=fake.numerify("#"*20))
#
#     contact_page.create_contact_steps(contact)
#
#
#     assert contact_page.get_alert_text().strip() == PHONE_ALERT_TEXT
#     contact_page.accept_alert()
#     assert contact_page.is_add_button_active()
#
#     contacts_page.open_contacts_list()
#     assert contacts_page.contact_cards_count(contact.phone) == 0def test_add_contact_invalid_phone_too_long(authenticated_driver):
#     contact_page = ContactPage(authenticated_driver)
#     contacts_page = ContactsPage(authenticated_driver)
#     contact = create_contact(phone=fake.numerify("#"*20))
#
#     contact_page.create_contact_steps(contact)
#
#
#     assert contact_page.get_alert_text().strip() == PHONE_ALERT_TEXT
#     contact_page.accept_alert()
#     assert contact_page.is_add_button_active()
#
#     contacts_page.open_contacts_list()
#     assert contacts_page.contact_cards_count(contact.phone) == 0
#
# def test_add_contact_invalid_phone_letters(authenticated_driver):
#     contact_page = ContactPage(authenticated_driver)
#     contacts_page = ContactsPage(authenticated_driver)
#     contact = create_contact(phone="jfhkdfghkfdh")
#
#     contact_page.create_contact_steps(contact)
#
#
#     assert contact_page.get_alert_text().strip() == PHONE_ALERT_TEXT
#     contact_page.accept_alert()
#     assert contact_page.is_add_button_active()
#
#     contacts_page.open_contacts_list()
#     assert contacts_page.contact_cards_count(contact.phone) == 0