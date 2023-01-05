# 3 Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import os
os.system("clear")
import math

my_list = [1.1, 1.2, 3.1, 5, 10.01]
my_list_2 = []

for i in range((len(my_list))):
     my_list_2.append(round(my_list[i] - int(my_list[i]), 2))

# if my_list_2[i] % 1 != 0:    
#     for i in range(len(my_list_2) - 1):
#         for j in range(len(my_list_2)-i-1):
#             if my_list_2[j] > my_list_2[j+1]:
#                 my_list_2[j], my_list_2[j+1] = my_list_2[j+1], my_list_2[j]
#     print(my_list_2)

if my_list_2[i] % 1 != 0:
    print(f'{my_list_2} -> {max(my_list_2) - min(my_list_2)}')