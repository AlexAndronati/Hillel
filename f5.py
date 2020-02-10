

def one_dimention(l):
    gl_l = []

    def recursa(l):
        for i in l:
            if isinstance(i, list):
                recursa(i)
            else:
                gl_l.append(i)
    recursa(l)
    return gl_l


li = [[], [1, 2], [2, 3, [1, 2]], [1, 2, [3]]]

print(one_dimention(li))

