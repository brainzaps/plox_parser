import sys
import os

from scanner import Scanner


class Lox:
    had_error = False

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

        if self.had_error:
            sys.exit(65)

    def run_prompt(self):
        while True:
            try:
                line = input("> ")
                self.run(line)
                self.had_error = False
            except KeyboardInterrupt:
                break
            except EOFError:
                break

    @staticmethod
    def run(source):
        tokens = Scanner(source).scan_tokens()

        for token in tokens:
            print(token)

    def error(self, line, message):
        self.report(line, "", message)

    @staticmethod
    def report(line, where, message):
        print(f"[line {line}] Error{where}: {message}")


def main():
    lox = Lox()


if __name__ == "__main__":
    main()
