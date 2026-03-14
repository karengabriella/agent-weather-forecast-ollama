import logging
import os
from datetime import datetime


def setup_logger(name="weather_agent"):
    os.makedirs("log", exist_ok=True)

    today = datetime.now().strftime("%Y-%m-%d")
    log_file = f"log/weather_agent_{today}.log"

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    logger.propagate = False

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger