import random
import string

def generate_password(length=8):
    if length < 6:
        raise ValueError("Минимальный пароль — шесть символов.")
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_login(length=8):
    if length < 3:
        raise ValueError("Длина логина должна быть не менее 3 символов.")
    characters = string.ascii_letters + string.digits
    login = ''.join(random.choice(characters) for _ in range(length))
    return f'{login}@ya.ru'

