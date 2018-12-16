# Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'z', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'z' включительно.

import random

print("Вычислим случайное целое число в указанном диапазоне")

min = int(input("Введите минимальное число: "))
max = int(input("Введите максимальное число: "))

integ = random.randint(0, max - min) + min

print("Случайное целое число в этом диапазоне: {}".format(integ))

flt = random.random() * (max - min) + min

print("Случайное вещественное число в этом диапазоне: {0:.2f}".format(flt))

s1 = ord(input("Введите первый символ: "))
s2 = ord(input("Введите второй символ: "))

symbol = random.randint(0, (s2 - s1)) + s1

print("Случайный символ в этом диапазоне: {}".format(chr(symbol)))