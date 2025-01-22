from loguru import logger


def setup_logging():
    logger.add("backup_redis.log", rotation="1 MB", retention="10 days")
    return logger
