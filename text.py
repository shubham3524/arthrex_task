from custom_logger import CustomLogger


logger = CustomLogger("app.log")


logger.debug("This is a debug message")
logger.info("This is an info message")
logger.error("This is an error message")