

class Range:

    def __init__(self, a, b=0, step=1):
        if b is self.__init__.__defaults__[0]:  # Имеет ли место быть такое решение?
                                                # или это можно сделать элегентнее?
            self.last = a
            self.current = 0
        else:
            self.current = a
            self.last = b
        self.step = step

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





