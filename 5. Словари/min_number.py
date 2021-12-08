"""
Программа принимает на вход словарь в JSON формате, значения являются целыми числами. Программа находит
минимальное значение по словарю и печатает ключ этого значения.

Sample Input: {"key1": 123, "key2": 11, "key3": 110000, "key4": 50}
Sample Output: key2
"""

import json
import operator

my_dict = json.loads(input())
print(min(my_dict.items(), key=operator.itemgetter(1))[0])