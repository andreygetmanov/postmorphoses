import sys
import os
import time


class Manifest:

    def __init__(self, length: int = 70, width: int = 14, pause: float = 1e-6):
        self.length = length
        self.width = width
        self.pause = pause

    @staticmethod
    def read_txt(file_path):
        with open(file_path, 'r', encoding="utf8") as f:
            return f.read()

    def print_one_by_one(self, char: str):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(self.pause)

    def print_data(self, content):
        os.system("")
        size = self.length * self.width
        k = 0
        while True:
            for word in content:
                for char in word:
                    if k == size:
                        self.print_one_by_one('\033[F'*(self.width - 1))
                        k = 0
                    self.print_one_by_one(char)
                    k += 1


if __name__ == '__main__':
    manifest = Manifest()
    content = manifest.read_txt('text.txt')
    manifest.print_data(content)

