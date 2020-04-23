import datetime
import itertools
import os
import string
# import threading
import multiprocessing
import time
# from queue import Queue
from multiprocessing import Queue
from zipfile import ZipFile


PROCESS_NUMBER = 5
found = False


def worker(q: Queue, num):
    print(f"Started worker {num}")
    global found
    with ZipFile(r"D:\Документы\Универ\Python\hillel\lesson6.zip", "r") as f:
        while not found:

            password = q.get()
            if password is None:
                break
            print(f"{password}\n", end="")
            try:
                # f.extractall("directory", pwd=password)

                f.extract(r"lesson6/file_16.txt", "directory", pwd=password)  # Не нашел как можно прочекать валидность
                                                                              # архива без извлечения из него файлов
                found = True

                print("ok")
                break
            except Exception as e:
                # found = False
                print(e)

    print(f"Finished worker {num}")


def generator(q: Queue):
    print(f"Started generator")

    global found
    gen = itertools.product(string.ascii_lowercase, repeat=3)  # генератор сочетаний с повторениями из 3х букв
    max_queue_size = 10
    for combination in gen:
        if found:
            break
        while q.qsize() > max_queue_size:
            time.sleep(0.0000001)
        combination = "".join(combination)
        combination = combination.encode('utf8')
        q.put(combination)
        # print(f"size = {q.qsize()}, comb = {combination}\n", end="")

    for i in range(PROCESS_NUMBER):
        q.put(None)
    print(f"Finished generator")


if __name__ == '__main__':
    start = datetime.datetime.now()

    multiprocessing.freeze_support()
    q = Queue()
    process_g = multiprocessing.Process(target=generator, args=(q,))
    # thread_g = threading.Thread(target=generator, args=(q,))
    workers = []
    for i in range(PROCESS_NUMBER):
        w = multiprocessing.Process(target=worker, args=(q, i))
        w.start()
        workers.append(w)

    process_g.start()
    process_g.join()

    for w in workers:
        w.join()
    finish = datetime.datetime.now() - start
    print(finish)
