# class User:
#     def __init__(self, email, password):
#         self.email=email
#         self.password=password

from dataclasses import dataclass, field

@dataclass
class User:
    username: str
    password: str = field(repr=False)  # Скрываем пароль из вывода repr

# Создаем экземпляр класса
user = User(username="admin", password="SecretPassword123")

# Печатаем объект
print(user)
        
