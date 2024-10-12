
'''
Написати бота, який буде порівнювати вік людини
'''


class TooYoungError(ValueError):
    pass


class NameTooShortError(Exception):
    pass


class SurnameTooShortError(ValueError):
    pass


def main():
    while True:
        age = int(input("Enter your age: "))
        if age < 18:
            # print("Too young")
            raise TooYoungError("Too young")
        name = input("Enter your name: ")
        if len(name) < 3:
            raise ValueError("Name is too short")
            # print("Name is too short")
        surname = input("Enter your surname: ")
        if len(surname) < 5:
            raise SurnameTooShortError("Surname is short")

try:
    main()
except TooYoungError:
    print("Young!")
except NameTooShortError:
    print("Too short!")
except ValueError as error:
    print(error)