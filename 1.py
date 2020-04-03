import os


def unique_generator(file_path):

    with open(file_path) as f:
        # u = unique()
        unique_set = set()
        for line in f:
            if line.strip() not in unique_set:
                print(line, end="")
                yield
                unique_set.add(line.strip())


if __name__ == '__main__':
    unique_generator("file1.txt")
    for _ in unique_generator("file1.txt"):
        pass
