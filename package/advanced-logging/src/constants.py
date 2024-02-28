# This file is a part of the advanced-logging package. It contains constants
# that are used throughout the package.

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

# Default Log Format.
DEFAULT_LOG_FORMAT = "[%(asctime)s - %(levelname)s - %(name)s]: %(message)s"