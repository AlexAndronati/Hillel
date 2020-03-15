from contextlib import contextmanager


def decorator_maker(*args):

    @contextmanager
    def suppress():
        try:
            yield "ok"
        except args:
            pass

    return suppress()


@decorator_maker(ZeroDivisionError, TypeError)
def spam():
    print(1/0)


@decorator_maker(ZeroDivisionError, TypeError)
def egg():
    print(1+"hi")


@decorator_maker(ZeroDivisionError, TypeError)
def foo():
    print([][3])


spam()
egg()
foo()
