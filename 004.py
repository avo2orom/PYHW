# 4 Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

number_of_quarter = int(input('Введите номер четверти от 1 до 4: '))

if number_of_quarter == 1:
    print('Диапазон возможных координат x > 0 and y > 0')
elif number_of_quarter == 2:
    print('Диапазон возможных координат x < 0 and y > 0')
elif number_of_quarter == 3:
     print('Диапазон возможных координат x < 0 and y < 0')
elif number_of_quarter == 4:
     print('Диапазон возможных координат x > 0 and y < 0')    
else:
    print('Ошибка ввода')

