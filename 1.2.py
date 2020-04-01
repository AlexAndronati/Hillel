

def my_range(*args):
    # if b is my_range.__defaults__[0]:
    #     last = a
    #     current = 0
    # else:
    #     current = a
    #     last = b
    #
    # step = step
    #
    if len(args) == 1:
        last = args[0]
        current = 0
        step = 1
    elif len(args) == 2:
        current = args[0]
        last = args[1]
        step = 1
    elif len(args) == 3:
        current = args[0]
        last = args[1]
        step = args[2]
    else:
        raise Exception("Number of arguments should be 1, 2 or 3")

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

    for i in my_range(7, 0):  # Начальное значение больше конечного. Ничего не выводит
        print(i, end=" ")
    print("\n")
    
    for i in my_range(1, 5, 2, 8):  # ERROR
        print(i, end=" ")
