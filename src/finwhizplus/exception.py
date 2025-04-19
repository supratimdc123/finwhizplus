from src.finwhizplus.logger import logger

class CustomException(Exception):
    def __init__(self, message, error: Exception):
        super().__init__(message)
        logger.error(f"{message}: {str(error)}")