import logging
import os

def setup_logging(module_name: str) -> logging.Logger:
    """Setup logging for the module."""
    os.makedirs("logs", exist_ok=True)
    logger = logging.getLogger(module_name)
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler("logs/etl_pipeline.log")
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
