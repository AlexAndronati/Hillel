


class Point(object):
    def __init__(self, x=0, y=0, z=0):
        self.y = y
        self.x = x
        self.z = z

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y, self.z+other.z)

    def __str__(self):
        return f"{self.x, self.y, self.z}"


if __name__ == '__main__':
    a = Point(0, 1, 2)
    b = Point(3, 2, 5)
    c = a+b
    print(c)
