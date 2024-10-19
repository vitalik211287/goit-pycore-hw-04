

# # def employees_generator(amount, x,y, z = ''):
# #       # Змінюємо ім'я змінної для генератора Faker
# #     users = []
    
# #     for i in range(int(amount)):
# #         mock = {
# #             "name": x(),
# #             "salary": y(2), 
# #         }
# #         users.append(mock)

# #     # Відкриваємо файл для запису і використовуємо метод write, а не writelines
# #     with open("users.json", "w") as file:
# #         file.write(json.dumps(users, indent=4))  # Записуємо дані у файл у форматі JSON з відступами
# #     return users
# # Викликаємо функцію


# # print(employees_generator(6, fake.name, fake.random_number))
# from faker import Faker
# import json, os, inspect
# fake = Faker()



# def employees_generator(amount, name, **kwargs):

#     salary_gen = kwargs.get('salary', Faker().random_number)
#     user_age = kwargs.get('age', Faker().random.randint)
#     user_id = kwargs.get('id', Faker().iban)
#     pet_name = kwargs.get('pet_name', Faker().first_name )

#       # Змінюємо ім'я змінної для генератора Faker
#     users = []
    
#     for i in range(int(amount)):
#         mock = {
#             "name": fake.name(),
#             "salary": salary_gen(2), 
#             "age": user_age(1,12),
#             "id" : user_id(),
#             "pet_name": pet_name()
#         }
#         users.append(mock)

#         # Отримуємо поточну директорію, де викликається скрипт
#     frame = inspect.currentframe()
#     frame = inspect.currentframe()  
#     caller_frame = frame.f_back  
#     caller_filename = caller_frame.f_code.co_filename 
#     current_dir =  os.path.dirname(caller_filename)   # Повертає поточну директорію
#     print(current_dir)
#     # Вказуємо шлях до файлу в поточній директорії
#     file_path = os.path.join(current_dir, "users.json")

#     # # Записуємо дані у файл JSON з відступами
#     with open(file_path, "w") as file:
#         file.write(json.dumps(users, indent=4))

#     # # Відкриваємо файл для запису і використовуємо метод write, а не writelines
#     with open("users.json", "w") as file:
#         file.write(json.dumps(users, indent=4))  # Записуємо дані у файл у форматі JSON з відступами
#     return users
# # Викликаємо функцію
# employees_generator(6,  
#     name = 'name', 
#     age = fake.random.randint, 
#     id = fake.iban, 
#     pet_name = fake.first_name  )

# # print(employees_generator
# #       (6, name = 'name',  
# #        pet_name = fake.pet  )) 
# def my_function():  
#     # Отримуємо інформацію про стек викликів  
#     frame = inspect.currentframe()  
#     caller_frame = frame.f_back  
#     caller_filename = caller_frame.f_code.co_filename  
    
#     # Отримуємо каталог, з якого викликалася функція  
#     caller_directory = os.path.dirname(caller_filename)  
    
#     print("Функція була викликана з каталогу:", caller_directory)  

# my_function()  

from faker import Faker  
import json  
import os  
import inspect  

fake = Faker()  

def save_to_json(data, filename):  
    #Записує дані у файл JSON з відступами
    with open(filename, "w") as file:  
        json.dump(data, file, indent=4)  

def employees_generator(amount, **kwargs):  
    #Генерує список котів  з випадковими даними  
    users = []  
    
    # Використовуємо один екземпляр Faker для генерації даних  
    user_age = kwargs.get('age', lambda: fake.random.randint(1, 12))  
    user_id = kwargs.get('id', lambda: fake.iban())  
    pet_name = kwargs.get('pet_name', lambda: fake.first_name())  

    for _ in range(int(amount)):  
        mock = {          
            "id": user_id(),  
            "pet_name": pet_name(),
            "age": user_age() 
        }  
        users.append(mock)  

    # Отримуємо каталог, з якого викликалася функція  
    current_dir = os.path.dirname(inspect.getfile(inspect.currentframe().f_back))  
    file_path = os.path.join(current_dir, "cats.json")  

    # Записуємо дані у файл  
    save_to_json(users, file_path)  
    # print(f"Дані збережено в: {file_path}")  

    return users  

# 