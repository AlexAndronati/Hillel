


def phone_decorator(func):

    def wrapper(l: list):
        li = []
        for i in l:
            s = "+91 " + i[-10:-5] + " " + i[-5:]
            li.append(s)
        f = func(li)
        return f

    return wrapper


@phone_decorator
def phone_sorter(l: list):
    return sorted(l)


def enter_data():
    n = int(input())
    phones = []
    for i in range(n):
        phone = input()
        phones.append(phone)
    return phones


if __name__ == "__main__":
    l = enter_data()
    print(l)
    print(phone_sorter(l))


"""
4
1234554321
9134554321
911234512345
01234554321
"""
