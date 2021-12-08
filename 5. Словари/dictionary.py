"""
Напиши код, который принимает на вход строку, в этой строке чётное количество слов, разделённых пробелами
(2, 4, 6, 8 или больше слов). Сформируй словарь таким образом, чтобы нечётные слова были ключами словаря,
а чётные — значениями по этим ключам.
Если количество слов нечётное — программа игнорирует последнее слово.

Sample Input 1: name Пётр phone 02 sex male balance 50000
Sample Output 1: {"name": "Пётр", "phone": "02", "sex": "male", "balance": "50000"}

Sample Input 2: 1 2 3 4
Sample Output 2: {"1": "2", "3": "4"}

Sample Input 3: 1 2 3
Sample Output 3: {"1": "2"}
"""

import json

my_dict = {}
dict_keys = []
dict_values = []
inp = input().strip().split(' ')

if len(inp) % 2 != 0:
    inp = inp[:len(inp) - 1]
for i in range(len(inp)):
    if i % 2 == 0:
        dict_keys.append(inp[i])
    else:
        dict_values.append(inp[i])
my_dict = dict(zip(dict_keys, dict_values))
print(json.dumps(my_dict, ensure_ascii=False))