

def zippp(*iterable):
    m = min(len(i) for i in iterable)
    for i in range(m):
        yield tuple(j[i] for j in iterable)


if __name__ == '__main__':

    a = [1, False, 3, 4, 8, 7]
    b = [2, 3, "hey", 5]
    c = range(3)

    t = zippp(a, b, c)

    for i in t:
        print(i)

