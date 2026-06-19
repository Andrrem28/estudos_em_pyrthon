from pathlib import Path

LOG_FILE = Path(__file__).parent / "log.txt"

class Log:
    def _log(self, message):
        raise NotImplementedError(
            "Implemente o método log"
        )
    
    def log_error(self, message):
        self._log(f"ERROR: {message}")

    def log_success(self, message):
        self._log(f"SUCCESS: {message}")

class LogFileMixin(Log):
    def _log(self, message):
        msg_file = f'{message} ({self.__class__.__name__})'
        with open(LOG_FILE, "a") as f:
            f.write(msg_file+ "\n")
        
class LogPrintMixin(Log):
    def _log(self, message):
        msg_print = f'{message} ({self.__class__.__name__})'
        with open(LOG_FILE, "a") as f:
            f.write(msg_print + "\n")

if __name__ == "__main__":
    lf = LogFileMixin()
    lp = LogPrintMixin()
    lf.log_error("Erro ao processar o arquivo")
    lp.log_success("Processamento concluído com sucesso")
    lf.log_success("Processamento concluído com sucesso")
    lp.log_error("Erro ao processar o arquivo")