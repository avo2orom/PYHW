# 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import os
os.system("clear")

def factorial(n):
    f = 1
    while n > 1:
        f *= n
        n -= 1
    return(f)


number = int(input('Введите число: '))
for item in range(1,number+1):
    print(factorial(item), end=" ")
