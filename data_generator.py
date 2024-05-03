from random import choice, randint
import string
import secrets
import names


def generate_password():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(6))
    return password


def generate_password_less_then5():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(1, randint(2, 6)))
    return password


def generate_email():
    return ''.join(choice(string.ascii_letters) for _ in range(10)) + "@yandex.ru"


def generate_name():
    return names.get_full_name()
