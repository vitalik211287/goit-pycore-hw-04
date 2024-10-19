

def parse_input(command_input):  
    args = command_input.strip().split()  # Розбиваємо ввід на частини  
    
    if not args:  
        return None, []  # Якщо немає аргументів, повертаємо None  
    
    # Повертаємо перший аргумент як команду та решту як аргументи  
    return args[0].strip().lower(), args[1:] 
