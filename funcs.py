l = [1, 1, 2, 2, 3,3, 4, 5, 5, 5, 5, 3, 5, 5, 7, 8, 9]
temp = 1
prev = l[0]
counts = {}
print(f"i = {prev}; prev = {prev}; temp = {temp}; counts = {counts}")
for i in l[1:]:
    if i == prev:
        temp += 1
    else:
        if counts.get(prev, -1) < temp:
            counts[prev] = temp
        temp = 1
    print(f"i = {i}; prev = {prev}; temp = {temp}; counts = {counts}")
    prev = i

if counts.get(prev, -1) < temp:
    counts[prev] = temp
print(f"prev = {prev}; temp = {temp}; counts = {counts}")

a = max(counts.values())
for i in counts:
    if counts.get(i) == a:
        print(i, a)

