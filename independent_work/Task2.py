s = input('Введите строку: ')

# Поиск и запись количества повторений элементов по алфавиту в словарь
d = {}
s = sorted(s)
for i in range(len(s)):
    sum = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            sum += 1
    d[s[i]] = sum
d1 = sorted(d)

# Вывод ответа
for key in d:
    print(str(key) + ' = ' + str(d[key]))
