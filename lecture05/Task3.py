import random

x = input('Введите положительное X: ')
max = input('Введите максимальное число: ')
min = input('Введите минимальное число: ')
b = input('Введите b: ')

# Блок проверки

if not(x.isdigit()):
    print('X - не положительное целое число')
    exit (1)
elif not(b.isdigit()):
    print('b - не целое число')
    exit (1)
elif not(max.isdigit()):
    print('Максимум - не целое число')
    exit (1)
elif not(min.isdigit()):
    print('Минимум - не целое число')
    exit (1)
else:
    x = int(x)
    b = int(b)
    max = int(max)
    min = int(min)
if not(min <= max):
    print('Минимальное число должно быть меньше максимального')
    exit (2)
elif not((b <= max) and (b >= min)):
    print('b должно лежать между ', str(min),' и ', str(max))
    exit (3)

# Блок вычислений и вывода

numbers = []
for _ in range(x):
    numbers.append(int(random.randint(min, max)))
print('Изначальный список:')
print(numbers)

b_numbers = []

for i in range(x):
    if numbers[i] != b:
        b_numbers.append(numbers[i])
print('Вывод списка без ', str(b), ':')
print(b_numbers)