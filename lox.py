import sys
import os

from scanner import Scanner
from error import LoxError


# sysexits.sh
# https://man.freebsd.org/cgi/man.cgi?query=sysexits&apropos=0&sektion=0&manpath=FreeBSD+4.3-RELEASE&format=html
class Lox:

    def __init__(self):
        if len(sys.argv) > 2:
            print("Usage: plox [script]")
            sys.exit(64)
        elif len(sys.argv) == 2:
            self.run_file(sys.argv[1])
        else:
            self.run_prompt()

    def run_file(self, file_path):
        path = os.path.abspath(file_path)
        with open(path, "r") as f:
            self.run(f.read())

        if LoxError.had_error:
            sys.exit(65)

    def run_prompt(self):
        while True:
            try:
                line = input("> ")
                self.run(line)
                LoxError.had_error = False
            except KeyboardInterrupt:
                break
            except EOFError:
                break

    @staticmethod
    def run(source):
        tokens = Scanner(source).scan_tokens()

        for token in tokens:
            print(token)
