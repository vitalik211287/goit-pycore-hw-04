from contacts import add_contact, change_contact, show_phone, show_all
from parser import parse_input

def main():
    print("Welcome to the assistant bot!")  # Вітання

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

