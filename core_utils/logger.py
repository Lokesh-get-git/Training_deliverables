import datetime
class Logger:
    Levels={
        "DEBUG":10,
        "INFO":20,
        "WARN":30,  
        "ERROR":40
    }

    def __init__(self,level="INFO",log_file=None):
        self.level=self.Levels[level]
        self.log_file=log_file

    def log(self,level,message):
        if self.Levels[level]<self.level:
            return
        timestamp=datetime.datetime.now().isoformat()
        log_line=f"[{timestamp}] [{level}] [{message}]"
        print(log_line)

        if self.log_file:
                with open(self.log_file,"a") as file:
                    file.write(log_line+"\n")
    def debug(self,message):
        self.log("DEBUG",message)
    def info(self,message):
        self.log("INFO",message)
    def warn(self,message):
        self.log("WARN",message)
    def error(self,message):
        self.log("ERROR",message)