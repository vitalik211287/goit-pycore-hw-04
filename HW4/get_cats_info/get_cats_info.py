from pathlib import Path
from faker import Faker 
import json
from employees_generator import employees_generator 
from read_json_file import read_json_file

def get_cats_info(path):

    fake = Faker()
    cats=[]

    # Перевіряємо, чи існує файл і читаємо дані  
    try:  
        templates = read_json_file(path)  
    except (FileNotFoundError, json.JSONDecodeError):  
        print("Файл не знайдено або містить помилки. Генеруємо нові дані.")  
    employees_generator(3,               
        id=lambda: fake.iban(),   
        pet_name=lambda: fake.first_name(),  
        age=lambda: fake.random.randint(1, 12))  
    templates = read_json_file(path)

    for cat in templates:    
        cats.append(cat)
    print(cats)   




path = Path('./HW4/get_cats_info/cats.json')
get_cats_info(path)