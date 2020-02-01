a = {'a': 1, 'b': 4, 't': 67}

b = {'c': 4, 'e': 1, 'a': 4, 't': 7, 'y': 11}

print("Список ключей, которые есть в обоих: ", b.keys() & a.keys())
print("Список ключей, которые есть только во 2-м: ", b.keys() - a.keys())

c = {}
c.update(a)
for i, j in b.items():
    if i not in c.keys():
        c.update({i: j})
    else:
        c[i] = c[i]+b[i]

print("Объединенный словарь: ", c)
