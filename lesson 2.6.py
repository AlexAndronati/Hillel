
s = "English = 78 Science = 83 Math = 68 History = 65"
s_list = s.split(" ")
count = sum([int(i) for i in s_list if i.isdecimal()])

print(count)
