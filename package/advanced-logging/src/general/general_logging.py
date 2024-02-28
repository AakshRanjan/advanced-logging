"""
    This module contains the general logging functions. It can be used to log
    messages in a flask application and etc.

    Author: Aaksh Ranjan
"""

import inspect
import logging

from . import constants

class GeneralLogging:

    def __init__(self, logger_name: str = None) -> None:
        """
        This function is used to initialize the GeneralLogging object.
        Args:
            logger_name (str): The name of the logger. DEFAULT: None.
        Output:
            NONE
        """
        if logger_name is None:
            logger_name = inspect.stack()[1].filename.split("/")[-1].split(".")[0]

        self.logger_name = logger_name

        # Create a logger object. Set the name of the logger to the name of the
        # file in which is GeneralLogger is being called, if logger_name is not provided.
        self.logger = logging.getLogger(logger_name)

    def config_file_logging(self) -> logging.Logger:
        """
        This function is used to create a logger object, which will direct the logs
        to the default file.

        Args:
           NONE
        Output:
            logger (logging.Logger): The logger object.
        """
        # Set the log levels to default file_paths.
        for log_level, file_path in constants.LOG_LEVELS.items():
            # Get the default file path for the log level.
            file_path = file_path.format(constants.DEFAULT_LOG_DIR.format(self.logger_name))

            # Create a file handler. If the file does not exist, create it.
            try:
                file_handler = logging.FileHandler(filename=file_path)
            except FileNotFoundError:
                with open(file_path, "w") as file:
                    pass
                file_handler = logging.FileHandler(filename=file_path)

            # Set the log level of the file handler.
            file_handler.setLevel(constants.LOG_LEVELS.get(log_level))

            # Add the file handler to the logger.
            self.logger.addHandler(file_handler)

        return self.logger

    def config_file_logging(self, config: dict) -> logging.Logger:
        """
        This function is used to create a logger object, which will direct the logs
        to the specified file.

        Args:
            config (dict): The configuration dictionary for log level to file path.
        Output:
            logger (logging.Logger): The logger object.
        """
        # If a log level is not specified in the configuration dictionary, set the defaults.
        default_log_levels = [
            log_level for log_level in constants.LOG_LEVELS if log_level not in config
        ]

        # Loop through the configuration dictionary.
        for log_level, file_path in config.items():
            # If the log level is not a valid log level, raise an error.
            if log_level not in constants.LOG_LEVELS:
                raise ValueError(f"Invalid log level: {log_level}")

            # Create a file handler. If the file does not exist, create it.
            try:
                file_handler = logging.FileHandler(filename=file_path)
            except FileNotFoundError:
                with open(file_path, "w") as file:
                    pass
                file_handler = logging.FileHandler(filename=file_path)

            # Set the log level of the file handler.
            file_handler.setLevel(constants.LOG_LEVELS.get(log_level))

            # Add the file handler to the logger.
            self.logger.addHandler(file_handler)

        # Set the log levels to default file_paths.
        for log_level in default_log_levels:
            # Get the default file path for the log level.
            file_path = file_path.format(constants.DEFAULT_LOG_DIR.format(self.logger_name))

            # Create a file handler. If the file does not exist, create it.
            try:
                file_handler = logging.FileHandler(filename=file_path)
            except FileNotFoundError:
                with open(file_path, "w") as file:
                    pass
                file_handler = logging.FileHandler(filename=file_path)

            # Set the log level of the file handler.
            file_handler.setLevel(constants.LOG_LEVELS.get(log_level))

            # Add the file handler to the logger.
            self.logger.addHandler(file_handler)

        return self.logger