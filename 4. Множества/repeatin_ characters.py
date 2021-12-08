"""
Напиши код, который убирает все повторяющиеся символы из этой строки и выводит на печать получившуюся строку.
Порядок символов должен сохраниться.

Sample Input: aaaaabbccddddddaaabbccee
Sample Output: abcde
"""

string = input()
new_string = ''.join(sorted(set(string), key=string.index))
print(new_string)