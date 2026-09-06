from pages.add_contact_page import ContactPage
from pages.contacts_page import ContactsPage


def test_delete_contact_decreases_list_by_one(ensure_min_contacts):
    contacts_page = ContactsPage(ensure_min_contacts)
    contacts_page.open_contacts_list()

    count_before = contacts_page.total_contacts_count()
    contacts_page.open_first_contact()
    contacts_page.submit_delete()

    count_after = contacts_page.total_contacts_count()
    assert count_after == count_before-1


def test_delete_all_contacts(ensure_min_contacts):
    contacts_page = ContactsPage(ensure_min_contacts)
    contacts_page.open_contacts_list()
    contacts_page.remove_all_contacts()
    assert contacts_page.total_contacts_count() == 0
