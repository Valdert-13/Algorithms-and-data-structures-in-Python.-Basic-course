# Задание №1

'''1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
то программа должна сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.'''

s = set ('+-*/')

while True:
    z = input("Введите знак (+, -, *, / или 0, если хотите завершить программу): ")
    if z != '0':
        if z in s:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            if z == '+':
                print(f'{a}+{b}={a+b}')
            elif z == '-':
                print(f'{a}-{b}={a-b}')
            elif z == '*':
                print(f'{a}*{b}={a*b}')
            elif z == '/':
                if b == 0:
                    print("На ноль делить нельзя!")
                else:
                    print(f'{a}/{b}={a/b}')
        else:
            print("Неверный знак")
    else:
        break