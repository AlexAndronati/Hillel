import random
while True:
    while True:
        length = input("Введите длину: ")
        if length.isdecimal() and int(length)>=0:
            break
        print("Вы ввели что-то не то: повторите")
    if int(length) == 0:
        break
    #65-90
    #97-122
    # 30-39
    alphabet = []
    password = []
    for i in range(ord("a"), ord("z")+1):
        alphabet.append(chr(i))
    for i in range(ord("A"), ord("Z")+1):
        alphabet.append(chr(i))
    for i in range(ord("0"), ord("9")+1):
        alphabet.append(chr(i))

    for i in range(int(length)):
        password.append(random.choice(alphabet))
    print("".join(password))
