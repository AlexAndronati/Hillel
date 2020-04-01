

class Range:

    def __init__(self, *args):
        if len(args) == 1:
            self.last = args[0]
            self.current = 0
            self.step = 1
        elif len(args) == 2:
            self.current = args[0]
            self.last = args[1]
            self.step = 1
        elif len(args) == 3:
            self.current = args[0]
            self.last = args[1]
            self.step = args[2]
        else:
            raise Exception("Number of arguments should be 1, 2 or 3")

    # def __init__(self, a, b=0, step=1):
    #     print(b is self.__init__.__defaults__[0])
    #     print(step is self.__init__.__defaults__[1])
    #
    #     if b is self.__init__.__defaults__[0]:  # Имеет ли место быть такое решение?
    #         # print(self.__init__.__defaults__)   # или это можно сделать элегентнее?
    #     # if b == 0:
    #         self.last = a
    #         self.current = 0
    #     else:
    #         self.current = a
    #         self.last = b
    #     self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.last:
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

    for i in Range(1, 5, 2, 8):  # ERROR
        print(i, end=" ")




