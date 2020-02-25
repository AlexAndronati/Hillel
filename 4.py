

with open(r"D:\Документы\Универ\Python\hillel\pract string\task4.txt", "r") as doc:
    gl_l = []
    for i in doc:
        i = i[:-1]
        l_i = i.split(" ")

        t = [i for i in l_i if 3 <= len(i) <= 5]
        print(i)
        print(t)

        ok = len(t)
        if ok % 2 == 1:
            t = t[:-1]

        l_i_new = []

        for j in l_i:
            if j not in t:
                l_i_new.append(j)

        print(f"!!!!!!{l_i_new}")
        print(ok, "\n")

        gl_l.append(" ".join(l_i_new))

with open(r"D:\Документы\Универ\Python\hillel\pract string\task4.txt", "w") as doc:
    for i in gl_l:
        doc.write(i)
        doc.write("\n")




# Original Data:
"""
London is the capital of Great Britain yes
Iron Maiden is the best heavy metal band in the world!
No
Yes
This is a string 
Wake up! Wrab a brush and put a little makeup!
"""