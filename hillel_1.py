
a = [1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2, 7, 43, 54, 13]

print(f"Maximum = {max(a)}, index = {a.index(max(a))}")
print(f"Minimum = {min(a)}, index = {a.index(min(a))}")

list_of_values = list(set(a))
list_of_values2 = list_of_values[:]

list_of_frequencies = []
for i in list_of_values:
    list_of_frequencies.append(a.count(i))

most_frequent_elements = []
for i in range(3):
    t = max(list_of_frequencies)
    t_i = list_of_frequencies.index(t)
    most_frequent_elements.append(list_of_values[t_i])
    del list_of_frequencies[t_i], list_of_values[t_i]

print("Самые частые элементы:", most_frequent_elements)

print("Список без повторений (без сохранения порядка): ", list_of_values2)

a_unique = []
for i in a:
    if i not in a_unique:
        a_unique.append(i)

print("Список без повторений (c сохранением порядка): ", a_unique)
