from faker import Faker
from models.contact import Contact

fake = Faker()

def create_contact(name = None, lastname = None, phone = None, email = None, address = None, description = None):
    return Contact(
        name = name if name is not None else fake.first_name(),
        lastname=lastname if lastname is not None else fake.last_name(),
        phone=phone if phone is not None else fake.unique.numerify("050##########"),
        email = email if email is not None else fake.unique.email(),
        address=address if address is not None else fake.street_address(),
        description=description if description is not None else fake.text()
    )

