# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

number_X = int(input('Введите координату точки X:\n'))
number_Y = int(input('Введите координату точки Y:\n'))
if number_X > 0 and number_Y > 0:
    print('Первая четверть')
elif number_X < 0 and number_Y > 0:
    print('Вторая четверть')
elif number_X < 0 and number_Y < 0:
    print('Третья четверть')
elif number_X > 0 and number_Y < 0:
    print('Четвертая четверть')
else:
    print('Введены некорректные данные')