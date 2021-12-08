"""
Напиши программу, которая принимает на вход два целочисленных числа, и, если оба больше 100, то выводит на печать
максимальное из них, в противном случае выводит на печать сумму второго числа и числа 112.
Sample Input: 11 50
Sample Output: 162
"""

numbers = input().strip().split(' ')
for number in numbers:
    if number.isalpha():
        exit('Нужны числа')
number_1, number_2 = map(int, numbers)
if number_1 > 100 and number_2 > 100:
    print(max(number_1, number_2))
else:
    print(number_2 + 112)