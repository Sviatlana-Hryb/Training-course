"""
Напиши программу, которая выводит на печать строку - Это положительное число, если на вход ей передано
целочисленное или нецелочисленное число, большее нуля. Разделитель дробной части может быть записан как точка
или как запятая (1.23 или 1,23).
Если на вход передан ноль, программа должна напечатать строку - Это ноль.
Если передано отрицательно число — программа должна напечатать строку - Это отрицательное число.
Sample Input: 1,288
Sample Output: Это положительное число
"""

inp_d = input().strip().replace(',', '.')
if inp_d.isalpha():
    exit('Нужно число')
elif float(inp_d) > 0:
    print('Это положительное число')
elif float(inp_d) == 0:
    print('Это ноль')
else:
    print('Это отрицательное число')