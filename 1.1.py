

class Range:

    def __init__(self, *args):
        self.step = 1

        if len(args) == 1:
            self.last = args[0]
            self.current = 0
        elif len(args) == 2:
            self.current = args[0]
            self.last = args[1]
        elif len(args) == 3:
            self.current = args[0]
            self.last = args[1]
            self.step = args[2]
        else:
            raise TypeError(f"range expected at most 3 arguments, got {len(args)}")

    def __iter__(self):
        return self

    def __next__(self):
        if self.step == 0:
            raise ValueError("Range() arg 3 must not be zero")

        if (self.current >= self.last and self.step > 0) or (self.current <= self.last and self.step < 0):
            raise StopIteration

        self.current += self.step
        return self.current-self.step


if __name__ == '__main__':

    for i in Range(11):
        print(i, end=" ")
    print("\n")

    for i in Range(3, 11):
        print(i, end=" ")
    print("\n")

    for i in Range(3, 11, 2):
        print(i, end=" ")
    print("\n")

    for i in Range(7, 0):  # Начальное значение больше конечного. Ничего не выводит
        print(i, end=" ")
    print("\n")

    for i in Range(11, 3, -1):
        print(i, end=" ")

    for i in Range(1, 5, 2, 8, 8):  # ERROR
        print(i, end=" ")




