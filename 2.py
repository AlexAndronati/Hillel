

class Reverse:
    def __init__(self, iterable):
        self.iterable = iterable
        self.current = len(iterable)-1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        self.current -= 1
        return self.iterable[self.current+1]


tu = (1, 2, "3aaa", 4, 5, [1, 2], 4)

print(list(Reverse(tu)))
