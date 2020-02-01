while True:
    n = int(input("Введите целое число: "))
    if not n:
        break

    numbers = list(range(2, n + 1))
    for i in numbers:
        if i != 0:
            for j in range(2 * i, n + 1, i):
                numbers[j - 2] = 0

    numbers = [i for i in numbers if i != 0]

    multipliers = []

    for i in numbers:
        while True:
            if n % i == 0:
                multipliers.append(i)
                n = n/i
            else:
                break

    multipliers_unique = []

    for i in multipliers:
        if i not in multipliers_unique:
            multipliers_unique.append(i)

    strings = []
    for i in multipliers_unique:
        if multipliers.count(i) > 1:
            strings.append(str(f"{i}^{multipliers.count(i)}"))
        else:
            strings.append(str(f"{i}"))

    s = " * ".join(strings)
    print(s)

