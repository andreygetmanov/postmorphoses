import sys
import os
import time


class Manifest:
    """
    A class for displaying text content in a scrolling fashion."""

    def __init__(self, length: int = 120, width: int = 30, pause: float = 0.07):
        """
        Initializes a new instance of the class.

            Args:
                length: The length of the bar. Defaults to 120.
                width: The width of the bar. Defaults to 30.
                pause: The pause duration between updates. Defaults to 0.07.

            Returns:
                None
        """
        self.length = length
        self.width = width
        self.pause = pause

    @staticmethod
    def read_txt(file_path):
        """
        Reads the content of a text file.

            Args:
                file_path: The path to the text file.

            Returns:
                str: The entire content of the file as a string.
        """
        with open(file_path, "r") as f:
            return f.read()

    def print_one_by_one(self, text: str):
        """
        Prints the given text character by character with a pause.

            Args:
                text: The string to be printed.

            Returns:
                None
        """
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(self.pause)
        sys.stdout.write(" ")

    def print_data(self, content):
        """
        Prints the given content to the console in a scrolling fashion.

            Args:
                content: A list of strings representing the data to be printed.

            Returns:
                None
        """
        # TODO loop console output
        os.system("")
        size = self.length * self.width
        k = 0
        while True:
            for word in content:
                for char in word:
                    if k == size:
                        self.print_one_by_one("\033[F" * (self.width - 1))
                        k = 0
                    self.print_one_by_one(char)
                    k += 1
