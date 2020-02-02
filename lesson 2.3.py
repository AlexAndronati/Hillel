
s = input("Введите строку: ")
s_reversed = "".join(reversed(list(s)))

if s == s_reversed:
    print("yes")
else:
    print("no")

