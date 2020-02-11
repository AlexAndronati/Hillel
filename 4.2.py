

def find_sum(target_list):
    suitable_list = []
    for i in range(len(target_list)):
        a = str(format(i, 'b'))  # представление в двоичном виде

        b = sum(int(j) for j in a if j != '-')  # поиск суммы
        #  print(i, " ", a, ": ", b)
        if not b % 2:
            suitable_list.append(target_list[i])
    #  print(suitable_list)

    return sum(suitable_list)


# l = [1, 2, 4, 6, 8, 9, 15, -4, -3, 14]
l = [1, 2, 3, 4, 5]
print(f"l = {l}")

#  print(find_sum(l))
result = find_sum(l)*l[-2]
print(f"sum = {result}")
