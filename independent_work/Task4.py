s = input('Введите дробь римскими числами в строку (числа от 1 до 999): ')

# Ввод словаря римских цифр

Rymnumb = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
Rymnumb_ftoppos = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90,
                   'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

# Проверка корректности ввода и преобразование римских цифер в арабские

fl = 0
numb_s = []
for elem in s:
    for key in Rymnumb:
        if elem == key:
            numb_s.append(Rymnumb[key])
            fl = 0
            break
        elif elem == '/':
            numb_s.append('/')
            fl = 0
            break
        else:
            fl = 1
    if fl == 1:
        print('ERROR')
        exit(1)

# Перевод римских чисел в арабские

first = []
second = []
i_palka = numb_s.index('/')
for i in range(len(numb_s)):
    if i < i_palka:
        first.append(numb_s[i])
    elif i > i_palka:
        second.append(numb_s[i])

symf = 0
syms = 0

for i in range(len(first)):
    if i == 0:
        if len(first) == 1:
            symf = first[i]
            break
        else:
            symf = first[i]
            continue
    elif first[i-1] < first[i]:
        symf += (first[i] - first[i-1]) - first[i-1]
        continue
    elif first[i-1] >= first[i]:
        symf += first[i]

for i in range(len(second)):
    if i == 0:
        if len(second) == 1:
            syms = second[i]
            break
        else:
            syms = second[i]
            continue
    elif second[i-1] < second[i]:
        syms += (second[i] - second[i-1]) - second[i-1]
        continue
    elif second[i-1] >= second[i]:
        syms += second[i]

# Сокращение дроби

number_f = symf
number_s = syms
while number_f != 0 and number_s != 0:
    if number_f > number_s:
        number_f = number_f % number_s
    else:
        number_s = number_s % number_f
NOD = number_f + number_s

symf = symf // NOD
syms = syms // NOD

# Перевод из арабских чисел в римские

romanNODf = ''
symfp = symf
while symfp != 0:
    for key, value in Rymnumb_ftoppos.items():
        if symfp < value:
            continue
        else:
            romanNODf = romanNODf + key
            if value == 1:
                symfp = symfp - value
                break
            else:
                symfp = symfp % value
                break

romanNODs = ''
symsp = syms
while symsp != 0:
    for key, value in Rymnumb_ftoppos.items():
        if symsp < value:
            continue
        else:
            romanNODs = romanNODs + key
            if value == 1:
                symsp = symsp - value
                break
            else:
                symsp = symsp % value
                break

# Вывод ответа

if romanNODs == 'I':
    print(romanNODf)
else:
    print(romanNODf + '/' + romanNODs)