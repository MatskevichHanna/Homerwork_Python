# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
#  и проверяет, является ли этот день выходным.
# Дополнительно: можете проверить, что это действительно число,
#  и что это действительно входит в нужный диапазон
# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day = int(input('Введите число от 1 до 7:\n'))
if day > 5 and day < 8:
    print('Да')
elif day > 0 and day < 6:
    print('Нет')
else:
    print('Ошибка, введите число от 1 до 7')