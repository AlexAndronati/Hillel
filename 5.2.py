l = [1, 1, 2, 2, 3,3, 4, 5, 5, 5, 5, 3, 5, 5, 7, 8, 9,9]


def RLE(l: list):
    temp = 1
    prev = l[0]
    new_list = []
    for i in l[1:]:
        if i == prev:
            temp += 1
        else:
            new_list.append((prev, temp))
            temp = 1
        prev = i

    new_list.append((prev, temp))
    return new_list
    # print(f"new list = {new_list}")

print(l)
print(RLE(l))