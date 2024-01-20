import sys
import os


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

    def run(self, source):
        pass

    def run_prompt(self):
        while True:
            line = input("> ")

            if not line:
                break

            self.run(line)


def main():
    lox = Lox()
    print("Hello World!")


if __name__ == "__main__":
    main()
