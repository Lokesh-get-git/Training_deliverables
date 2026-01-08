import datetime
class Logger:
    Levels={
        "DEBUG":10,
        "INFO":20,
        "ERROR":40
    }
    def __init__(self,level="INFO",log_file=None):
        self.level=self.Levels[level]
        self.log_file=log_file
