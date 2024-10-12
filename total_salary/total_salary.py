from pathlib import Path
import json
import sys
from employees_generator import employees_generator

path = Path('./users.json')

def total_salary(path):
    # Перевіряємо, чи існує файл
    if not path.exists():
        print(f"Файл {path} не існує.")
        sys.exit(1)

    try:
        # Читаємо файл, якщо він існує     
        with open(f'{path}', 'r') as f:
            file_content = f.read()           
            templates = json.loads(file_content)

    except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
        # Обробляємо випадок, коли файл відсутній або зламаний
        print(f"Помилка при читанні файлу: {e}.")
        sys.exit(1)

# Обчислюємо загальну кількість співробітників        
    len_path = int(len(templates))
    total = 0

# Підраховуємо загальну зарплату
    for i in templates:
            path_salary = int(i.get('salary'))
            total += path_salary

 # Обчислюємо середню зарплату       
    if len_path != 0:
        average = round((total / len_path), 3)
        return f'Загальна сума заробітної плати: {total}, середня заробітна плата: {average}'
    else:
        return "Помилка: неможливо обчислити середнє, оскільки в списку немає жодного працівника."
        
   


print(total_salary(path))