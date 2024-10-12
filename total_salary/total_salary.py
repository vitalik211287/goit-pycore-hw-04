from pathlib import Path
import json
import employees_generator

path = Path('./users.json')

def total_salary(path):
    with open(f'{path}') as f:
        file_content = f.read()
        templates = json.loads(file_content)
    len_path = int(len(templates))
    total = 0
    for i in templates:
        path_salary = int(i.get('salary'))
        total = total + path_salary
    average = round((total / len_path),3)
    return f'Загальна сума заробітної плати {total}, середня заробітна плата {average}'  




print(total_salary(path))