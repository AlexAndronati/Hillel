import string

alphabet = string.ascii_lowercase


def rangoli(n: int):
    s = alphabet[:n]
    s = s[::-1]+s[1:]
    s = "-".join(list(s))
    rangoli_list = []
    rangoli_list.append(s)

    for i in range(n-1):
        s = "--"+s[:int((n-1)*2)-2] + s[-int((n-1)*2)+1:]+"--"
        rangoli_list.append(s)
        rangoli_list.insert(0, s)

    print(*rangoli_list, sep="\n")


if __name__ == '__main__':
    a = int(input())
    rangoli(a)
