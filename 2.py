
with open(r"D:\Документы\Универ\Python\hillel\pract string\document.txt") as doc:
    with open (r"D:\Документы\Универ\Python\hillel\pract string\document2.txt", "w") as file:
        for i in doc:
            j = i.split("\t")
            print(j)
            if j[1][0] in ('K', 'C'):
                file.write(f"{j[0]} {j[1][:-1]}\n")

