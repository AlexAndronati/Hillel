

def decorator_maker(max_size):

    def decorator(func):
        cache = {}
        calls = 0
        taken_from_cache = 0

        def wrapper(n):
            nonlocal cache
            nonlocal calls
            nonlocal taken_from_cache

            calls += 1
            if n not in cache:
                cache[n] = func(n)
            else:
                taken_from_cache += 1
                cache.pop(n)
                cache[n] = func(n)

            if len(cache) > max_size:
                cache.pop(list(cache.keys())[0])# displacement of the less used element

            #print(cache)

            return cache[n]

        def cache_clear():
            cache.clear()

        def cache_info():
            print(f"size of cache is {len(cache)}")
            print("Number of function calls = ", calls)
            print("Number of function calls, where the value was taken from cache = ", taken_from_cache)

        wrapper.cache_clear = cache_clear
        wrapper.cache_info = cache_info
        return wrapper

    return decorator


@decorator_maker(5)
def my_func(n):
    return n**2


if __name__ == "__main__":
    print(my_func(10))
    print(my_func(8))
    print(my_func(5))
    my_func.cache_info()
    print(my_func(2))
    print(my_func(1))
    print(my_func(10))
    print(my_func(6))

    my_func.cache_clear()
    print(my_func(6))
    my_func.cache_info()
