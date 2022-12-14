# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x_coordinate = int(input('Введите координату точки по x: '))
y_coordinate = int(input('Введите координату точки по y: '))
if x_coordinate and y_coordinate !=0:
    if x_coordinate and y_coordinate > 0:
        print(f'Точка с координатами {x_coordinate} и {y_coordinate} находится в I четверти плоскости')
    elif x_coordinate < 0 and y_coordinate > 0:
        print(f'Точка с координатами {x_coordinate} и {y_coordinate} находится во II четверти плоскости')
    elif x_coordinate < 0 and y_coordinate < 0:
        print(f'Точка с координатами {x_coordinate} и {y_coordinate} находится во III четверти плоскости')
    elif x_coordinate > 0 and y_coordinate < 0:
        print(f'Точка с координатами {x_coordinate} и {y_coordinate} находится во IV четверти плоскости')
    
