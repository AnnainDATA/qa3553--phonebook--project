from faker import Faker

fake = Faker()
print(fake.first_name())
print(fake.last_name())

print(fake.email())
print(fake.unique.email()) #не повторяет значения!

print(fake.phone_number())
print(fake.numerify("05##########"))

print(fake.sentence())



