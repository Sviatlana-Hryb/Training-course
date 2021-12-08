"""
Напиши программу, которая считает стоимость доставки для транспортной компании.
Цена каждых 100 грамм уменьшается с общим увеличением веса посылки. При отправке до 500г каждые 100г посылки
стоят 80 рублей, при отправке свыше 1000 грамм каждые 100г стоят 65 рублей.

Программа принимает вес в граммах на вход. При некорректном весе программа печатает: некорректный вес.

При весе более 10кг программа печатает: не возим.
"""

import math

weight = input().strip()

if not weight.isdigit():
    print('некорректный вес')
elif int(weight) > 10000:
    print('не возим')
elif int(weight) <= 500:
    weight = int(weight)
    tax = math.ceil(weight / 100) * 80
    print(tax)
elif 500 < int(weight) <= 1000:
    weight = int(weight)
    tax = math.ceil(weight / 100) * 70
    print(tax)
elif 1000 < int(weight) <= 10000:
    weight = int(weight)
    tax = math.ceil(weight / 100) * 65
    print(tax)