"""
Напиши функцию is_password_hard, которая принимает на вход пароль и возвращает True, если он надёжный
или False в противном случае.
Надёжным считаем пароль, длина которого 12 и больше символов, который содержит хотя бы 1 букву в большом
регистре, хотя бы 1 букву в маленьком регистре и хотя бы одну цифру.
"""

import re

def is_password_hard(password: str) -> bool:
    if len(password) < 12:
        return False
    else:
        down_register_pattern = re.search('[a-z]', password)
        up_register_pattern = re.search('[A-Z]', password)
        is_digit_pattern = re.search('[\d]', password)
        if down_register_pattern and up_register_pattern and is_digit_pattern:
            return True
        else:
            return False