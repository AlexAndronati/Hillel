

def singleton(cls):

    first_call = {}

    def wrapper(*args, **kwargs):
        if cls not in first_call:
            first_call[cls] = cls(*args, **kwargs)
        return first_call[cls]

    return wrapper


@singleton
class A(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.__dict__}"


if __name__ == '__main__':
    abc = A(3, 5)
    print(abc)
    aaa = A(7, 6)
    print(aaa)

