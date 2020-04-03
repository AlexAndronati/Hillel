import os


def path_generator(path_to_directory):
    for dirpath, dirnames, filenames in os.walk(path_to_directory):
        for filename in filenames:
            yield "\\".join([dirpath, filename])


if __name__ == '__main__':
    [print(i) for i in path_generator(r"D:\Документы\концерты")]




