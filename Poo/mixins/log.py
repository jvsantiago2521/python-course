import os
os.system("cls")

#Abstracao

class Log:
    def _log(self):
        raise NotImplementedError("Implemente o metodo log!")
    
    def log_error(self, msg):
        return self._log(f"Error: {msg}")

    def log_error(self, msg):
        return self._log(f"Sucess: {msg}")

class LogFileMixin(Log):
    def _log(self, msg):
        print(msg)

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f"{msg} {self.__class__.__name__}")
    
if __name__ == "__main__":
    l = LogPrintMixin()
    l.log_error("ERRO")
