class LoxError:
    had_error = False

    @staticmethod
    def error(line, message):
        LoxError.report(line, "", message)

    @staticmethod
    def report(line, where, message):
        print(f"[line {line}] Error{where}: {message}")
