# s = "spam and eggs or eggs with spam"
s = input("Введите строку: ")

print("Before: ", s)
s_list = s.split(" ")
s_list = ["".join(reversed(list(i))) for i in s_list]
s = " ".join(s_list)
print("After: ", s)
