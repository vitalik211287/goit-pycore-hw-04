from faker import Faker  
import json  
import os  
import inspect  

fake = Faker()  

def save_to_json(data, filename):  
# Записує дані у файл JSON з відступами
    with open(filename, "w") as file:  
        json.dump(data, file, indent=4)  

def employees_generator(amount, **kwargs):  
# Генерує список співробітників з випадковими даними
    users = []  
 
    salary_gen = kwargs.get('salary', Faker().random_number)
    user_age = kwargs.get('age', Faker().random.randint)
    user_id = kwargs.get('id', Faker().iban)
    pet_name = kwargs.get('pet_name', Faker().first_name )

    for _ in range(int(amount)):  
        mock = {  
            "name": fake.name(),  
            "salary": salary_gen(),   
            "age": user_age(),  
            "id": user_id(),  
            "pet_name": pet_name()  
        }  
        users.append(mock)  

    # Отримуємо каталог, з якого викликалася функція  
    current_dir = os.path.dirname(inspect.getfile(inspect.currentframe().f_back))  
    file_path = os.path.join(current_dir, "users.json")  

    # Записуємо дані у файл  
    save_to_json(users, file_path)  

    return users  
