import math
import itertools


class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)

    def findS(self, other):
        h = other.x - self.x
        side1 = other.y
        side2 = self.y
        trapezium_midline = (side1+side2)/2

        return trapezium_midline * h


class Polygon:

    def __init__(self, l: list):
        self.l = l

    def findPS(self, func):  # применяет функцию func ко всем парам

        c = itertools.cycle(self.l)
        prev = next(c)
        polygon_S = 0

        for i in range(len(self.l)):
            cur = next(c)
            p = Point(prev[0], prev[1])
            p2 = Point(cur[0], cur[1])
            prev = cur

            polygon_S += func(p, p2)

        return polygon_S

    def P(self):
        return self.findPS(Point.distance)

    def S(self):
        return self.findPS(Point.findS)


if __name__ == '__main__':
    p = Polygon([
        (2, 3),
        (2, 5),
        (4, 5),
        (4, 7),
        (7, 3),
        (7, 2),
        (6, 2),
        (6, 3),
    ])
    print(p.P())
    print(p.S())


