import random

n = 20
a = input('Введите число A: ')

# Блок проверки

fA = a
fl = 0
if '.' in fA:
    fl = 1
    fA = fA.replace('.','')
if '-' in fA:
    fA = fA.replace('-','')
if not(fA.isdigit()):
    print('A - не число')
    exit (1)
if fl != 0:
    a = float(a)
else:
    a = int(a)

# Блок вычислений

numbers = []
bnumbers = []
for i in range(n):
    numbers.append(random.uniform(0, 100))
    bnumbers.append(random.uniform(0, 100))
    bnumbers[i] = int(bnumbers[i] * 1000) / 1000
    numbers[i] = int(numbers[i] * 1000) / 1000
    numbers[i] = int((numbers[i] - bnumbers[i]) * 1000) / 1000
print('Изначальный список:')
print(numbers)

sort = sorted(numbers)

sum = 0
amount = 0
for i in range(n):
    if numbers[i] > a and numbers[i] < 0:
        sum += numbers[i]
        amount += 1

# Блок вывода

print('Сумма всех отрицательных чисел до ' + str(a) +': ' + str(sum))
print('Количество всех отрицательных чисел до ' + str(a) +': ' + str(amount))