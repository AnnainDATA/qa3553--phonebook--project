import random
from models.contact import Contact
from pages.add_contact_page import ContactPage
from faker import Faker
fake=Faker()


def test_add_contact_success_all_field(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)

    randon_suffix = random.randint(1,10000000)
    contact=Contact(
        name = fake.first_name(),
        lastname = fake.last_name(),
        phone = fake.numerify("05##########"),
        email = f"anna_test_{randon_suffix}@gmail.com",
        address = "Tel Aviv",
        description = "QA lesson contact"
    )
    print(randon_suffix)

    contact_page.open_contacts_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert contact_page.contact_card_visible(contact.phone)
#-------------------------------------------------------------------
def test_add_contact_success_required_field(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)

    randon_suffix = random.randint(1,10000000)
    contact=Contact(
        "Anna",
        "Karenina",
        f"05012{randon_suffix}",
        f"anna_test_{randon_suffix}@gmail.com",
        "Tel Aviv",
        ""
    )
    #print(randon_suffix)

    contact_page.open_contacts_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert contact_page.contact_card_visible(contact.phone)


