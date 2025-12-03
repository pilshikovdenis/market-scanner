import json
import logging
import os
from pathlib import Path
from colorama import init, Fore, Style

init()


class ColoredFormatter(logging.Formatter):
    COLORS = {
        logging.DEBUG: Fore.CYAN,
        logging.INFO: Fore.GREEN,
        logging.WARNING: Fore.YELLOW,
        logging.ERROR: Fore.RED,
        logging.CRITICAL: Fore.RED + Style.BRIGHT,
    }

    def format(self, record):
        log_color = self.COLORS.get(record.levelno, Fore.WHITE)
        message = super().format(record)
        return f"{log_color}{message}{Style.RESET_ALL}"


def load_config(config_path="config.json"):
    config_file = Path(config_path)
    if not config_file.exists():
        raise FileNotFoundError(f"Конфигурационный файл не найден: {config_path}")

    with open(config_file, "r", encoding="utf-8") as f:
        config = json.load(f)

    log_dir = Path(config.get("log_dir", "."))
    log_dir.mkdir(parents=True, exist_ok=True)

    return config


def create_colored_console_logger(name=None, level=logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.handlers.clear()

    handler = logging.StreamHandler()
    handler.setLevel(level)
    formatter = ColoredFormatter(
        '%(asctime)s | %(levelname)s | %(name)s | %(message)s',
        datefmt='%H:%M:%S'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


def create_file_logger(name=None, log_dir=".", log_file="app.log", level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.handlers.clear()

    log_path = Path(log_dir) / log_file

    handler = logging.FileHandler(log_path, encoding="utf-8")
    handler.setLevel(level)
    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)s | %(name)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


def setup_logger(name=None):
    config = load_config()

    if config["debug"]:
        level = getattr(logging, config["console_level"], logging.DEBUG)
        return create_colored_console_logger(name, level)
    else:
        level = getattr(logging, config["file_level"], logging.INFO)
        log_dir = config.get("log_dir", ".")
        log_file = config["log_file"]
        return create_file_logger(name, log_dir, log_file, level)
