import traceback


class MyException(Exception):

    def __init__(self, text):
        self.text = text

    def write_to_file(self):
        with open("file1.txt", 'a') as f:
            f.write(f"args = {self.args}\ntraceback = ")
            traceback.print_tb(self.__traceback__, file=f)
            f.write("\n")


if __name__ == '__main__':
    try:
        raise MyException("Ooops")
    except MyException as e:
        e.write_to_file()
