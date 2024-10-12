from pathlib import Path
import json
from employees_generator import employees_generator

path = Path('./users.json')

def total_salary(path):
    # Перевіряємо, чи існує файл
    if not path.exists():
        print(f"Файл {path} не існує. Генеруємо новий список співробітників.")
        employees_generator(6)  # Генеруємо 6 співробітників, якщо файл відсутній
    
    try:
        # Читаємо файл, якщо він існує
        with open(f'{path}', 'r') as f:
            file_content = f.read()
            if not file_content.strip():  # Перевірка, чи не порожній файл
                raise ValueError("Файл порожній. Генеруємо нові дані.")
            
            templates = json.loads(file_content)

    except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
        # Обробляємо випадок, коли файл відсутній або зламаний
        print(f"Помилка при читанні файлу: {e}. Генеруємо нові дані.")
        employees_generator(6)
        with open(f'{path}', 'r') as f:
            templates = json.load(f)

    # Обчислюємо загальну кількість співробітників
    len_path = int(len(templates))
    total = 0

    # Підраховуємо загальну зарплату
    for i in templates:
        path_salary = int(i.get('salary'))
        total += path_salary

    # Обчислюємо середню зарплату
    average = round((total / len_path), 3)

    return f'Загальна сума заробітної плати {total}, середня заробітна плата {average}'


# Виклик функції
print(total_salary(path))
