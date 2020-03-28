

def my_range(a, b=0, step=1):
    if b is my_range.__defaults__[0]:
        last = a
        current = 0
    else:
        current = a
        last = b

    step = step
    while current < last:
        yield current
        current += step


if __name__ == '__main__':

    for i in my_range(11):
        print(i, end=" ")
    print("\n")
    for i in my_range(3, 11):
        print(i, end=" ")
    print("\n")

    for i in my_range(3, 11, 2):
        print(i, end=" ")
    print("\n")

    





