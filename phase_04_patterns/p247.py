class RealLogger:
    def log(self, message):
        print(message)


class NullLogger:
    def log(self, message):
        pass

def process(data, logger):
    if logger is not None:   
        logger.log("Processing started")

real = RealLogger()
process("data", real)

null = NullLogger()
process("data", null)