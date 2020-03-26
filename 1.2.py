
class ClassMethod:
    def __init__(self, method):
        self.method = method

    def __get__(self, instance, owner):
        def foo(*args):
            return self.method(owner, *args)
        return foo


class A:

    @ClassMethod
    def foo(cls, *args):
        print(cls, *args)


if __name__ == '__main__':
    a = A()
    a.foo(7, "ok")
    A.foo(7, "ok")
