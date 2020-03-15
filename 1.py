from contextlib import contextmanager


@contextmanager
def suppress_decorator():
    try:
        yield "ok"
    except Exception as e:
        pass


class Suppress:
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True


def zero_div():
    print("before trying to divide by 0")
    print(1/0)


if __name__ == '__main__':

    with Suppress() as s:
        zero_div()

    print("ok")

    with suppress_decorator():
        zero_div()

    print("ok")
