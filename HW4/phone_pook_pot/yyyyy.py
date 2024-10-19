# Словник для зберігання контактів  
contacts = {}  

# Функція для парсингу команд та аргументів з вводу  
def parse_input(command_input):  
    args = command_input.strip().split()  # Розбиваємо ввід на частини  
    
    if not args:  
        return None, []  # Якщо немає аргументів, повертаємо None  
    
    # Повертаємо перший аргумент як команду та решту як аргументи  
    return args[0].strip().lower(), args[1:]  

# Функція для додавання контакту  
def add_contact(args):  
    if len(args) == 2:  
        name, phone = args  
        contacts[name] = phone  
        return f"Contact {name} added."  
    else:  
        return "Error: Please provide both a name and a phone number."  

# Функція для зміни контакту  
def change_contact(args):  
    if len(args) == 2:  
        name, new_phone = args  
        if name in contacts:  
            contacts[name] = new_phone  
            return f"Contact {name} updated."  
        else:  
            return f"Error: Contact {name} not found."  
    else:  
        return "Error: Please provide both a name and a new phone number."  

# Функція для показу номера телефону  
def show_phone(args):  
    if len(args) == 1:  
        name = args[0]  
        if name in contacts:  
            return f"{name}'s phone number is {contacts[name]}."  
        else:  
            return f"Error: Contact {name} not found."  
    else:  
        return "Error: Please provide a contact name."  

# Функція для показу всіх контактів  
def show_all():  
    if contacts:  
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])  
    else:  
        return "No contacts found."  

# Основна функція  
def main():  
    print("Welcome to the assistant bot!")  # Додаємо вітання  

    while True:  
        command_input = input("Enter a command: ")  # Отримуємо команду від користувача  
        command, args = parse_input(command_input)  # Використання функції parse_input()  
        
        if command in ["close", "exit"]:  
            print("Good bye!")  
            break  
        elif command == "hello":  
            print("How can I help you?")  
        elif command == "add":  
            print(add_contact(args))  
        elif command == "change":  
            print(change_contact(args))  
        elif command == "phone":  
            print(show_phone(args))  
        elif command == "all":  
            print(show_all())  
        else:  
            print("Invalid command.")  

if __name__ == "__main__":  
    main()