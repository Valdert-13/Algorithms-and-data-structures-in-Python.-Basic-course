# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

# вариант 1
num = int(input("Введите количество чисел: "))
digit = int(input("Какую цифру подсчитать: "))
count = 0
for i in range(1, num + 1):
    ans = int(input(f'Введите число {i}: '))
    while ans > 0:
        if ans % 10 == digit:
            count += 1
        ans //= 10

print(f'Было введено {count} цифр {digit}')


# вариант 2
num = int(input("Введите количество чисел: "))
digit = input("Какую цифру подсчитать: ")
count = 0
for i in range(1, num + 1):
    ans = input(f'Введите число {i}: ')
    count += ans.count(digit)

print(f'Было введено {count} цифр {digit}')
