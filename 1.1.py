import datetime
import multiprocessing as mp
from multiprocessing import Queue
import time

PROC_NUMBER = 2


def is_prime(num):
    if num <= 2:
        return True

    if num % 2 == 0:
        return False

    for i in range(3, int(num ** 0.5 + 1)):
        if num % i == 0:
            return False

    return True


def worker(q: Queue, num):

    while True:
        temp = q.get()
        if temp is None:
            break
        if is_prime(temp):
            print(f"{num}: {temp}")


def generator(q: Queue):
    max_size = 50
    for i in range(1_000_000):
        while q.qsize() > max_size:
            time.sleep(0.000001)
        q.put(i)
    for i in range(PROC_NUMBER):
        q.put(None)


if __name__ == '__main__':
    # mp.freeze_support()

    start = datetime.datetime.now()

    q = Queue()
    p = mp.Process(target=generator, args=(q,))

    workers = []

    for i in range(PROC_NUMBER):
        w = mp.Process(target=worker, args=(q, i))
        w.start()
        workers.append(w)
    p.start()

    p.join()

    for worker in workers:
        worker.join()

    print(datetime.datetime.now()-start)
