import collections
l = [1, 2, 3, 4, 5]
l2 = l[:]
n = int(input("Enter the shift: "))


# Shift without deque
# l2 = []
# l2.extend(l[-n:])
# l2.extend(l[:-n])
# print(l2)

for i in range(abs(n)):
    if n < 0:
        t = l.pop(0)
        l.append(t)
    else:
        t = l.pop()
        l.insert(0,t)

print(l)

l3 = collections.deque(l2)
l3.rotate(n)
print(l3)
