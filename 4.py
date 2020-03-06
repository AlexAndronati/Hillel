import os
import json


class JsonWorker:

    @staticmethod
    def write(path, data):
        with open(path, "w") as f:
            json.dump(data, f, indent=3)

    @staticmethod
    def read(path):
        with open(path, "r") as f:
            data = json.load(f)
        return data

    @staticmethod
    def combine(path_destination, path_sources: tuple):
        d = {}
        for path in path_sources:
            with open(path, "r") as f:
                d.update(json.load(f))
        with open(path_destination, "w") as f1:
            json.dump(d, f1, indent=3)

        return d

    @staticmethod
    def absolutePath(path):
        return os.path.abspath(path) # Это ведь так надо делать?

    @staticmethod
    def relativePath(path):
        return os.path.relpath(path)


if __name__ == '__main__':

    d = {
        1.0: "a",
        2: None,
        3: {"s": "st", "u": "uv"}
    }

    d2 = {
        10.0: "aaa",
        20: 4,
        15: {"sss": "st", "uuu": "uv"}
    }

    JsonWorker.write(r"file1.json", d)
    JsonWorker.write(r"file2.json", d2)
    print(JsonWorker.read(r"file1.json"))
    print(JsonWorker.read(r"file2.json"))
    # twmp = j.combine(r"destination_file.json", (r"file1.json", r"file2.json"))
    # print(twmp)
    print(JsonWorker.absolutePath(r"file1.json"))
    print(JsonWorker.relativePath(r"file1.json"))



