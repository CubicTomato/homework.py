import random

n = 10

# Ввод списка

numbers = []
for _ in range(n):
    numbers.append(int(random.randint(1, 10)))
print('Изначальный список:')
print(numbers)

# Сортировка и обозначение элементов

sort = sorted(numbers)
max = sort[-1]
min = sort[0]
imax = []
imin = []
iall = []
answer = []
di = []
i_numbers = []

# Поиск всех индексов минимальных и максимальных элементов

for i in range(n):
    if numbers[i] == max:
        imax.append(i)
    elif numbers[i] == min:
        imin.append(i)

# Вывод всех индексов минимальных и максимальных элементов (оставлено для удобства)
print(imax)
print(imin)

# Выбор определённого кода через количество индексов каждого вида (по флагам fl)

if len(imax) >= len(imin):
    u = len(imax)
    o = len(imin)
    fl = 1
elif len(imax) <= len(imin):
    u = len(imin)
    o = len(imax)
    fl = 2
else:
    u = len(imax)
    fl = 3

# Запись в ответ всех вариантов выбора определённых максимального и минимального элементов

i = 0
if fl == 1:
    for i in range(u):
        for y in range(o):
            if imax[i] >= imin[y]:
                i_numbers = []
                for j in range(n):
                    if not(imin[y] < j and j < imax[i]):
                        i_numbers.append(numbers[j])
                answer.append(i_numbers)
            elif imax[i] <= imin[y]:
                i_numbers = []
                for j in range(n):
                    if not(imin[y] > j and j > imax[i]):
                        i_numbers.append(numbers[j])
                answer.append(i_numbers)
elif fl == 2:
    for y in range(u):
        for i in range(o):
            if imax[i] >= imin[y]:
                i_numbers = []
                for j in range(n):
                    if not(imin[y] < j and j < imax[i]):
                        i_numbers.append(numbers[j])
                answer.append(i_numbers)
            elif imax[i] <= imin[y]:
                i_numbers = []
                for j in range(n):
                    if not(imin[y] > j and j > imax[i]):
                        i_numbers.append(numbers[j])
                answer.append(i_numbers)
elif fl == 3:
    for y in range(u):
        for i in range(u):
            if imax[i] >= imin[y]:
                i_numbers = []
                for j in range(n):
                    if not(imin[y] < j and j < imax[i]):
                        i_numbers.append(numbers[j])
                answer.append(i_numbers)
            elif imax[i] <= imin[y]:
                i_numbers = []
                for j in range(n):
                    if not(imin[y] > j and j > imax[i]):
                        i_numbers.append(numbers[j])
                answer.append(i_numbers)

# Вывод ответа

print('Ответ для любых варианций выбора максимального и минимального элементов:')
for i in range(len(answer)):
    print(str(answer[i]))