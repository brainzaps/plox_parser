class ErrorReporter:
    had_error = False

    def __init__(self, tag=None):
        self.tag = tag

    def error(self, line, message):
        self.report(line, "", message)

    @staticmethod
    def report(line, where, message):
        print(f"[line {line}] Error{where}: {message}")

    def __str__(self):
        return f"ErrorReporter(tag={self.tag}, had_error={self.had_error})"
