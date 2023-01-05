# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

import os
os.system("clear")

import random

num = int(input('Введите количество элементов в последовательности: '))
my_list = []
for i in range(num):
    my_list.append(random.randint(-num, num)) # не нужно последнее значние +1
print(my_list)

with open('file.txt', 'w') as data:
    n1 = input('Укажите первую позицию элемента: ')
    data.write(f'{n1}\n')
    n2 = input('Укажите вторую позицию элемента: ')
    data.write(n2)


path = 'file.txt'
data = open(path, 'r')
   
multipli = 1

for line in data:
    print(f'Элемент с индексом {line} равен {my_list[int(line)]}')
    multipli *=my_list[int(line)]

print(f'\nУмножение элементов равняется: {multipli}')