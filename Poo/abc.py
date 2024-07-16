from abc import ABC, abstractmethod

class Log(ABC):
    @abstractmethod
    def _log(self):...

    def log_error(self, msg):
        return self._log(f"Error: {msg}")

    def log_sucess(self, msg):
        return self._log(f"Sucess: {msg}")

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f"{msg} ({self.__class__.__name__})")

l = LogPrintMixin()
l.log_error("ERROR")

l2 = LogPrintMixin()
l2.log_sucess("SUCESS")

