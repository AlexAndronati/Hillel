
def min(*args):
    minimum = args[0]
    for i in args[1:]:
        if i < minimum:
            minimum = i
    return minimum

l = [1, 2, 7, -4, 6, -10, 4, 5]


print(min(1, 2, 7, -4, 6, -10, 4, 5))

print(min(l))

