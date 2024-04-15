import logging
import logging.handlers
import os
import threading

class CustomLogger:
    def __init__(self, log_file):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(thread)d - %(message)s')
        
        # Rotating file handler
        self.handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=10)
        self.handler.setFormatter(formatter)
        self.logger.addHandler(self.handler)
        
        # Lock to ensure thread safety
        self.lock = threading.Lock()
    
    def debug(self, msg):
        with self.lock:
            self.logger.debug(msg)
    
    def info(self, msg):
        with self.lock:
            self.logger.info(msg)
    
    def error(self, msg):
        with self.lock:
            self.logger.error(msg)

# Usage example
if __name__ == "__main__":
    logger = CustomLogger("app.log")
    logger.debug("Debug message")
    logger.info("Info message")
    logger.error("Error message")







   


