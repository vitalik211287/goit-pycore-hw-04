import sys
from pathlib import Path
from colorama import init, Fore

# Ініціалізація colorama для підтримки кольорового виведення
init(autoreset=True)

def show_directory_structure(directory_path):
    directory = Path(directory_path)

    # Перевірка чи існує шлях і чи він є директорією
    if not directory.exists() or not directory.is_dir():
        print(Fore.RED + "Помилка: вказаний шлях не є директорією або не існує.")
        return

    print(Fore.YELLOW + f"Структура директорії: {directory_path}\n")
    
    # Функція для виведення структури директорії
    def recursive_directory_traversal(current_directory, indent_level=0):
        for item in current_directory.iterdir():  # Перебираємо всі елементи у директорії
            indent = "  " * indent_level  # Додаємо відступ для вкладених елементів

            if item.is_dir():
                # Якщо це директорія, виводимо її імена зеленим кольором
                print(Fore.GREEN + indent + f"📂 {item.name}")
                # Рекурсивно проходимо всередину піддиректорії
                recursive_directory_traversal(item, indent_level + 1)
            else:
                # Якщо це файл, виводимо його ім'я синім кольором
                print(Fore.BLUE + indent + f"📜 {item.name}")

    # Запускаємо рекурсивну функцію для кореневої директорії
    recursive_directory_traversal(directory)

# Отримуємо шлях до директорії з аргументів командного рядка


path = sys.argv[1]
show_directory_structure(path)
