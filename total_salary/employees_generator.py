from faker import Faker
import json


def employees_generator(amount):
    fake = Faker()  # Змінюємо ім'я змінної для генератора Faker
    users = []
    
    for i in range(int(amount)):
        mock = {
            "name": fake.name(),
            "salary": fake.random_number(2)
        }
        users.append(mock)
    
    # print(users)
    
    # Відкриваємо файл для запису і використовуємо метод write, а не writelines
    with open("users.json", "w") as file:
        file.write(json.dumps(users, indent=4))  # Записуємо дані у файл у форматі JSON з відступами
    return users
# Викликаємо функцію
list_employees = employees_generator(6)