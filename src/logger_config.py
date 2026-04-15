#logger centralized to avoid duplication (Singleton design pattern)

import loggin
import sys
import os
from pathlib import Path

def get_logger(name: str) -> loggin.Logger:
    """
    Centralized console to pipelline logs
    """

    log_level_str = os.getenv("LOG_LEVEL","INFO".upper()
    log_level = getattr(logging, log_level_str, logging.INFO) [cite:302]

    logger = logging.getLogger(name) #Singleton

    if logger.handlers:
        return logger
   
    logger.setLevel(log_level) [cite:308]
    
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(name)-20s | %(levelname)-8s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S" [cite: 317, 318]
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    log_dir = Path("data")
    log_dir.mkdir(parents=True, exist_ok=True)
    
    file_handler = logging.FileHandler(log_dir / "pipeline.log", encoding="utf-8")

    file_handler.setLevel(logging.DEBUG) 
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger
