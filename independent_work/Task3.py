s = input('Введите строку: ')


# Разделение строки и сортировка букв по алфавиту
slist = s.split()
first = sorted(slist[0].lower())
second = sorted(slist[1].lower())

# Проверка корректности ввода
if not(slist[0].isalpha() and slist[1].isalpha()):
    print('Введите слова')
    exit(1)

# Сравнение букв двух слов
d = {}
for i in range(len(first)):
    sum = 0
    for j in range(len(second)):
        if first[i] == second[j]:
            sum += 1
            break
    d[first[i]] = sum

# Вывод ответа
result = []
for key in d:
    if d[key] >= 1:
        result.append(key)
print(' '.join(result))