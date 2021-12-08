"""
Измени программу (файл: dictionary) так, чтобы в полученном словаре значение ключа special_key было равно 12.

Sample Input: name Пётр phone 02 sex male balance 50000
Sample Output: {"name": "Пётр", "phone": "02", "sex": "male", "balance": "50000", "special_key": 12}
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
my_dict["special_key"] = 12
print(json.dumps(my_dict, ensure_ascii=False))