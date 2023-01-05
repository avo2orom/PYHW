# 4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
import os
os.system("clear")

number = int(input(("Введите число: ")))

count = ''
while (number > 0):
    count = str(number % 2) + count
    number = number // 2
print(count)

