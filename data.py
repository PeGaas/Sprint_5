from random import randint, choice
import string
import secrets


NAME = "Petr Gaas"
EMAIL = f"petergaas8{randint(100, 999)}@yandex.ru"
PASSWORD = '123456'
INVALID_PASSWORD = '12345'


def generate_password():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(6))
    return password


def generate_email():
    return ''.join(choice(string.ascii_letters) for _ in range(10)) + "@yandex.ru"
