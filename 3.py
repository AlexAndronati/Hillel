from time import time,sleep


class ManaDec:

    def __enter__(self):
        self.beginning = time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time()
        print(f"Runtime = {end-self.beginning}")
        return True

    def __call__(self, func):
        self.func = func

        def wrapper(*args):
            beginning = time()
            f = self.func(*args)
            end = time()
            print(f"Runtime = {end-beginning}")

            return f

        return wrapper


@ManaDec()
def foo():
    sleep(3)


if __name__ == '__main__':

    a = 1
    b = 0

    with ManaDec() as md:
        for i in range(1_000_000):
            if b != 0:
                c = a/b

    with ManaDec() as md:
        for i in range(1_000_000):
            try:
                c = a / b
            except ZeroDivisionError as e:
                pass
