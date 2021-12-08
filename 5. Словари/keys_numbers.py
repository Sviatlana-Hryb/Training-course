"""
Программа принимает на вход целочисленное число, назовём его для примера n. Надо сформировать словарь, ключами
которого будут числа от 1 по n (то есть включая n), а значения будут равны ключу, возведенному в квадрат.

Sample Input 1: 1
Sample Output 1: {"1": 1}

Sample Input 2: 2
Sample Output 2: {"1": 1, "2": 4}

Sample Input 3: 5
Sample Output 3: {"1": 1, "2": 4, "3": 9, "4": 16, "5": 25}
"""

import json

inp = input().strip()
if not inp.isdigit():
    print('передайте число')
    exit()
dict = {}
inp = int(inp)
for i in range(1, inp + 1):
    dict[i] = i ** 2

print(json.dumps(dict, ensure_ascii=False))
