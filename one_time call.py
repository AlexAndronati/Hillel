
def tracer_decorator(to_decorate):
    called = False

    def wrapper(*args, **kwargs):
        nonlocal called
        if not called:
            res = to_decorate(*args, **kwargs)
            called = True
            return res
        else:
            return "The function was already called once!"

    return wrapper


@tracer_decorator
def foo(a: int):
    return [i**1000/((i+1)**950) for i in range(a)]


print(foo(100))
print(foo(100))
print(foo(100))
