"""
Напиши функцию numbers_to_text, которая принимает на вход строку в виде последовательности цифр и пробелов,
и переводит эту последовательность в текст кириллицей (абвгд...).  Например, строка  2 означает одинарное
нажатие кнопки 2, что соответствует кириллической букве «а». Строка 22 соответствует двойному нажатию
на кнопку 2, это буква «б». Строка 222 соответствует тройному нажатию на кнопку 2, это буква «в» и так далее.

Строка 2222 2 222 означает «гав». Пробел между цифрами в коде означает паузу, то есть окончание ввода конкретной буквы.

Полный набор команд приведён ниже:
1	. , ? ! : ;
2	а б в г
3	д е ж з
4	и й к л
5	м н о п
6	р с т у
7	ф х ц ч
8	ш щ ъ ы
9	ь э ю я
0	символ пробела
Регистр текста — всегда нижний.

Если набор цифр некорректный (например, на вход переданы без пробела 123 или 9999999), функция
возвращает None, в противном случае функция возвращает текстовый результат.
"""

from typing import Optional

legend = {
    "1": ".,?!:;",
    "2": "абвг",
    "3": "дежз",
    "4": "ийкл",
    "5": "мноп",
    "6": "рсту",
    "7": "фхцч",
    "8": "шщъы",
    "9": "ьэюя",
    "0": " "
}

def numbers_to_text(numbers: str) -> Optional[str]:
    text = numbers.split()
    for index, word in enumerate(text):
        if len(set(word)) != 1:
            return None
        text[index] = legend[word[0]][len(word) - 1]

    return "".join(text)