from loguru import logger
import sys

def get_logger():
    logger.remove()
    logger.add(
        sys.stdout,
        level="INFO",
        format="<green>{time}</green> | <level>{level}</level> | <cyan>{message}</cyan>"
    )
    return logger
