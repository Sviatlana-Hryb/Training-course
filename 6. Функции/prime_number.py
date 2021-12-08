"""
Напиши функцию get_next_prime_number, которая принимает на вход целое положительное число и возвращает первое простое
число, большее заданного, и функцию is_prime_number, которая проверяет, является ли переданное ей число простым.

Простое число — это число, которое делится без остатка только на себя и на единицу. Примером могут быть
числа 2, 3, 5, 7, 11 и так далее.
"""

def get_next_prime_number(number: int) -> int:
    number += 1
    check = (is_prime_number(number))
    while (True):
        if (check == False):
            number += 1
            check = (is_prime_number(number))
        else:
            break
    return number

def is_prime_number(number: int) -> bool:
    check = 0
    if number == 1 or number == 2:
        check = True
        return check

    for i in range(2, number):
        if number % i == 0:
            return (False)
            break
        else:
            check = "True"
    return check
