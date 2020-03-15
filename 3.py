import time


class RuntimeCalculator:
    def __init__(self):
        self.beginning = time.time()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        ending = time.time()
        self.runtime_calc = ending - self.beginning


if __name__ == '__main__':

    with RuntimeCalculator() as r:
        for i in range(1000000):
            temp = i**25-i**24.5

    print(r)
    print(r.runtime_calc)

