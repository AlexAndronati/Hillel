s = "Help Elephant Learn LOops. While's and fOrs. RLD"

l = []
for i in s:
    if i.isupper():
        l.append(i)

print("".join(l))
