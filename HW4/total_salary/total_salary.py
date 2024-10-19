from pathlib import Path
import sys  
from faker import Faker
from employees_generator import employees_generator
from read_json_file import read_json_file


path = Path('./HW4/total_salary/users.json')

def total_salary(path):
    fake = Faker()
# Перевіряємо, чи існує файл
    if not path.exists():
        print(f"Файл {path} не існує, введіть інший шлях")
        sys.exit(1)
    try:        
# Читаємо файл, якщо він існує     
         templates = read_json_file(path)
    except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
        
# Обробляємо випадок, коли файл відсутній або зламаний
        print(f"Помилка при читанні файлу: {e}.")
        sys.exit(1)

# Обчислюємо загальну кількість співробітників        
    len_path = int(len(templates))
    total = 0

# Перевірка, чи не порожній файл
    if len_path == 0:
        print("Файл порожній. Генеруємо нові дані.")
    employees_generator(6,   
            salary=lambda: fake.random_number(3),   
            age=lambda: fake.random.randint(1, 12),   
            id=lambda: fake.iban(),   
            pet_name=lambda: fake.first_name()  )   
    templates = read_json_file(path)

# Підраховуємо загальну зарплату
    for i in templates:
        path_salary = int(i['salary'])
        total += path_salary

 # Обчислюємо середню зарплату       
    average = round((total / int(len(templates))), 3) if templates else 0

    return f'Загальна сума заробітної плати: {total}, середня заробітна плата: {average}'


print(total_salary(path))