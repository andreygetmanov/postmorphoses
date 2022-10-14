import sys
import os
import time


class Manifest:

    def __init__(self, length: int = 120, width: int = 30, pause: float = 0.07):
        self.length = length
        self.width = width
        self.pause = pause

    @staticmethod
    def read_txt(file_path):
        with open(file_path, 'r') as f:
            return f.read()

    def print_one_by_one(self, text: str):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(self.pause)
        sys.stdout.write(' ')

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
