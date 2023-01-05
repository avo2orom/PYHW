# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# *Пример:*
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

import os
os.system("clear")

# n = int(input('Введите число: '))
# lst = [round((1+1/i)**i, 3) 

# for i in range(1, n+1)]
# print(f'Последовательность: {lst}')

n = int(input('Введите число: '))
seq = dict()
seq_sum = 0
for i in range(1, n+1):
    seq[i] = round((1+1/i)**i, 2)
print(f'Для числа {n}  {seq}')
print(f'Сумма {sum(seq.values())}')