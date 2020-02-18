import functools


def decorator(to_decorate):
    @functools.wraps(to_decorate)
    def wrapper(*args, **kwargs):
        res = to_decorate(*args, **kwargs)
        return res

    return wrapper


@decorator
def foo(a: int):
    """
    The Docstring
    :param a:
    :return:
    """

    return a**2


print(foo(2))
print(foo.__doc__)
