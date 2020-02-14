

def longest_sequence(l: list):
    temp = 1
    prev = l[0]
    counts = {}
    for i in l[1:]:
        if i == prev:
            temp += 1
        else:
            if counts.get(prev, -1) < temp:
                counts[prev] = temp
            temp = 1
        prev = i

    if counts.get(prev, -1) < temp:
        counts[prev] = temp

    # print(f"counts = {counts}")
    a = max(counts.values())
    for i in counts:
        if counts.get(i) == a:
            # print(f"'{i}' - {a}")
            break
    return i, a


l = [1, 1, 2, 2, 3, 3, 4, 5, 5, 5, 5, 3, 5, 5, 7, 8, 9]
print(f"list: {l}")

print(f"'{longest_sequence(l)[0]}' - {longest_sequence(l)[1]}")
