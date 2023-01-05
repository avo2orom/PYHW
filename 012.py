# 2 Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
import os
os.system("clear")


num = int(input('Введите количество элементов в последовательности: '))
my_list = []
for i in range(num):
    my_list.append(random.randint(0, 10))
print(f'Последовательность: {my_list}')
my_list_2 = []

def MulElementsInArr(my_list, my_list_2):
    
    for i in range(int(len(my_list) // 2 + len(my_list) % 2)):
        my_list_2.append(my_list[i] * my_list[-(i + 1)])
    return my_list_2

print(f'Произведение пар чисел списка: {MulElementsInArr(my_list, my_list_2)}')