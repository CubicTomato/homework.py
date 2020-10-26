import random

n = 10

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

posit = 0
negat = 0
pamount = 0
namount = 0
for i in range(n):
    if numbers[i] > 0:
        posit += numbers[i]
        pamount += 1
    elif numbers[i] < 0:
        negat += numbers[i]
        namount += 1

mposit = posit / pamount
mnegat = negat / namount

# Блок вывода

print('Среднее арифметическое всех положительных чисел: ' + str(mposit))
print('Среднее арифметическое всех отрицательных чисел: ' + str(mnegat))
