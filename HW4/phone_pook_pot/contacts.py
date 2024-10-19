contacts = {}

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