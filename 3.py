
def capitalize(s):
    s = list(s)
    if s[0].isalpha():
        s[0] = s[0].upper()
    for i in range(1, len(s[1:])+1):
        if s[i-1] == " " and s[i].isalpha():
            s[i] = s[i].upper()
    return "".join(s)


if __name__ == "__main__":
    name = input()
    print(capitalize(name))
