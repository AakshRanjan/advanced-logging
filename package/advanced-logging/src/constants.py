# This file is a part of the advanced-logging package. It contains constants
# that are used throughout the package.

import logging

# Types of log levels.
LOG_LEVELS = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
}

# Default Log Level to File Path Configuration.
DEFAULT_LOG_DIR = "/var/log/{}"
DEFAULT_LOG_LEVEL_TO_FILE_PATH = {
    "DEBUG": "{}/debug.log",
    "INFO": "{}/info.log",
    "WARNING": "{}/warning.log",
    "ERROR": "{}/error.log",
    "CRITICAL": "{}/critical.log",
}

# Default Log Format General.
DEFAULT_LOG_FORMAT = "[%(asctime)s - %(levelname)s - %(name)s]: %(message)s"
DEFAULT_LOG_LEVEL_TO_FORMAT = {
    "DEBUG": DEFAULT_LOG_FORMAT,
    "INFO": DEFAULT_LOG_FORMAT,
    "WARNING": DEFAULT_LOG_FORMAT,
    "ERROR": DEFAULT_LOG_FORMAT,
    "CRITICAL": DEFAULT_LOG_FORMAT,
}

# Default Log Format for Flask.
DEFAULT_LOG_FORMAT_FLASK = "[%(asctime)s - %(levelname)s - %(name)s - %(request_id)s]: %(message)s"
DEFAULT_LOG_LEVEL_TO_FORMAT_FLASK = {
    "DEBUG": DEFAULT_LOG_FORMAT_FLASK,
    "INFO": DEFAULT_LOG_FORMAT_FLASK,
    "WARNING": DEFAULT_LOG_FORMAT_FLASK,
    "ERROR": DEFAULT_LOG_FORMAT_FLASK,
    "CRITICAL": DEFAULT_LOG_FORMAT_FLASK,
}