from datetime import datetime

class Logger:
    def __init__(self, name):
        self.name = name

    def log(self, level, message):
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"[{ts}] [{self.name}] [{level}] {message}"
        print(line)

        with open("app.log", "a") as f:
            f.write(line + "\n")

    def info(self, msg):
        self.log("INFO", msg)

    def warning(self, msg):
        self.log("WARNING", msg)

    def error(self, msg):
        self.log("ERROR", msg)


def get_logger(name):
    return Logger(name)


def log_button_click(logger, label):
    logger.info(f"Button clicked -> {label}")
