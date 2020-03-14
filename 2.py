from contextlib import contextmanager
from time import sleep, time


@contextmanager
def foo():
    beginning = time()

    try:
        yield None
    except Exception:
        pass
    end = time()
    print("Time: ", end - beginning)


if __name__ == '__main__':

    with foo() as f:

        for i in range(2):
            sleep(1)

