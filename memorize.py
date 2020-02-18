import time


def time_decorator(to_decorate):

    def wrapper(*args, **kwargs):
        t = time.time()
        res = to_decorate(*args, **kwargs)
        print(f"Runtime: {time.time()-t}")
        return res
    return wrapper


def memory_decorator(to_decorate):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = to_decorate(*args)
        return cache[args]
    return wrapper


def tracer_decorator(to_decorate):
    traces = 0

    def wrapper(*args, **kwargs):
        nonlocal traces
        traces += 1
        print(f"Function was called {traces} times")
        res = to_decorate(*args, **kwargs)
        return res
    return wrapper


@time_decorator
@tracer_decorator
@memory_decorator
def foo(a: int):
    return [i**1000/((i+1)**950) for i in range(a)]




print(foo(100))
print(foo(100))
print(foo(100))
