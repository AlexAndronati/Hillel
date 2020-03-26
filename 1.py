
class StaticMethod:
    def __init__(self, method):
        self.method = method

    def __get__(self, instance, owner):
        return self.method


class A:
    @StaticMethod
    def func(a):
        return a+1


a = A()
print(a.func(6))
print(A.func(6))