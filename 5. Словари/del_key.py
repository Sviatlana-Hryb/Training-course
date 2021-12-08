"""
Если в словаре есть ключ special_key, удали его и выведи на печать получившийся словарь,
если нет — просто выведи исходный словарь.

Sample Input: {"key1": 1, "key2": 11, "key3": 110000, "key4": 50}
Sample Output: {"key1": 1, "key2": 11, "key3": 110000, "key4": 50}
"""

import json
my_dict = json.loads(input().strip())
if 'special_key' in my_dict.keys():
    my_dict.pop('special_key')
print(json.dumps(my_dict, ensure_ascii=False))