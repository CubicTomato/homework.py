import random

x = 20
max = input('Введите максимальное число: ')
min = input('Введите минимальное число: ')
A1 = input('Введите A1: ')
A2 = input('Введите A2: ')
A3 = input('Введите A3: ')

# Блок проверки

fA1 = A1
fA2 = A2
fA3 = A3
fl = 0         # Обозначение fl - флаг
flA1 = 0
flA2 = 0
flA3 = 0
if '.' in fA1 or '.' in fA2 or '.' in fA3:
    fl = 1
    if '.' in fA1:
        flA1 = 1
        fA1 = fA1.replace('.','')
    if '.' in fA2:
        flA2 = 1
        fA2 = fA2.replace('.','')
    if '.' in fA3:
        flA3 = 1
        fA3 = fA3.replace('.','')
if not(max.isdigit()):
    print('Максимум - не целое число')
    exit (1)
elif not(min.isdigit()):
    print('Минимум - не целое число')
    exit (1)
elif not(fA1.isdigit()):
    print('A1 - не число')
    exit (1)
elif not(fA2.isdigit()):
    print('А2 - не число')
    exit (1)
elif not(fA3.isdigit()):
    print('A3 - не число')
    exit (1)
else:
    max = int(max)
    min = int(min)
    if fl != 0:
        if flA1 == 1:
            A1 = float(A1)
        else:
            A1 = int(A1)
        if flA2 == 1:
            A2 = float(A2)
        else:
            A2 = int(A2)
        if flA3 == 1:
            A3 = float(A3)
        else:
            A3 = int(A3)
if not(min <= max):
    print('Минимальное число должно быть меньше максимального')
    exit (2)
elif not((A1 <= max) and (A1 >= min) or (A2 <= max) and (A2 >= min) or (A3 <= max) and (A3 >= min)):
    print('Числа A1, A2, A3 должны лежать между ', str(min),' и ', str(max))
    exit (3)

# Блок вычислений и вывода

numbers = []
for _ in range(x):
    numbers.append(int(random.randint(min, max)))
print('Изначальный список:')
print(numbers)

numbers[2] = A1
numbers[3] = A2
numbers[4] = A3
print('Вывод списка c числами А1(' + str(A1) + '), А2(' + str(A2) + '), А3(' + str(A3) + '):')
print(numbers)