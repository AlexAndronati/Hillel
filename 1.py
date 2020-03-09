import math


class Figure (object):
    def P(self):
        raise Exception("No")

    def S(self):
        raise Exception("No")


class Triangle(Figure):
    def __init__(self, a: list):
        if len(a) != 3:
            raise Exception("Not a triangle")

        if a[0]+a[1] < a[2] or a[1]+a[2] < a[0] or a[0]+a[2] < a[1]:
            raise Exception("Not a triangle")

        self.a = a[0]
        self.b = a[1]
        self.c = a[2]

    def P(self):
        return self.a+self.b+self.c

    def S(self):
        p = self.P()/2
        S_Geron = math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
        return S_Geron


class Rectangle(Figure):

    def __init__(self, a: list):
        if len(a) != 2:
            raise Exception("Not a rectangle")
        self.a = a[0]
        self.b = a[1]

    def P(self):
        return 2*(self.a + self.b)

    def S(self):
        return self.a * self.b


class Circle(Figure):

    def __init__(self, r):
        self.r = r

    def P(self):
        return 2*math.pi*self.r

    def S(self):
        return math.pi * self.r**2


if __name__ == '__main__':
    t = Triangle([3, 4, 5])
    print(t.P())
    print(t.S())
    c = Circle(3)
    print(c.P())
    print(c.S())


