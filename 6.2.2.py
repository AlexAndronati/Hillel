
from functools import singledispatch

@singledispatch
def foo(a):
    print(f"We don't know the type of {a}")


@foo.register(int)
def _(a):
    print(f"The type of {a} is int")


@foo.register(float)
def _(a):
    print(f"The type of {a} is float")


@foo.register(str)
def _(a):
    print(f"The type of {a} is string")


foo([2, 3])
foo(5)
foo(5.)
