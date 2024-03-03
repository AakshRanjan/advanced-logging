"""
    This module contains the general logging functions. It can be used to log
    messages in a flask application and etc.

    Author: Aaksh Ranjan
"""

import inspect
import logging
import os

from typing import Tuple, Union

from . import constants, Utils


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

    def single_format_logging(self, log_format: str = str()) -> logging.Logger:
        """
        This function is used to configure the log format of the logger to a single format.
        If no log format is provided, the default log format will be used. If the logger doesn't
        have any handlers, a stream handler will be added to the logger to set the log format.

        Args:
            log_format (str): The log format string. DEFAULT: DEFAULT_LOG_FORMAT.
        Output:
            logger (logging.Logger): The logger object.
        """
        # If the log format is not provided, set the default log format.
        if not log_format:
            log_format = constants.DEFAULT_LOG_FORMAT

        # If no handlers are present, create a stream handler to set the log format.
        if len(self.logger.handlers) == 0:
            # Create a stream handler.
            handler = logging.StreamHandler()

            # Create a formatter object.
            formatter = logging.Formatter(log_format)

            # Set the formatter to the handler.
            handler.setFormatter(formatter)

            # Add the handler to the logger.
            self.logger.addHandler(handler)

            return self.logger

        # If handlers are present, set the log format for each handler.
        # Loop through the handlers of the logger.
        for handler in self.logger.handlers:

            # Create a formatter object.
            formatter = logging.Formatter(log_format)

            # Set the formatter to the logger.
            handler.setFormatter(formatter)

        return self.logger

    def multi_format_logging(self, config: dict = dict()) -> logging.Logger:
        """
        This function is used to configure the log format of the logger to multiple formats.
        If no log format is provided for a log level, the default log format will be used.
        If the logger doesn't have a handler for a log level, a stream handler will be added
        to the logger to set the log format. If a handler for a log level exists, the log format
        will be set for the handler. If no log format is provided for a log level, the default log
        format will be used.

        Args:
            config (dict): The configuration dictionary for log level to log format. DEFAULT: dict().
        Output:
            logger (logging.Logger): The logger object.
        """
        # Loop through the configuration dictionary.
        for log_level, log_format in config.items():
            # If the log level is not a valid log level, raise an error.
            if log_level not in constants.LOG_LEVELS:
                raise ValueError(f"Invalid log level: {log_level}")

            # If the log format is None or empty string, set the default log format.
            if not log_format:
                # Get the default log format for the log level.
                log_format = constants.DEFAULT_LOG_FORMAT

            # If no handlers are present, create a stream handler for that log level to set the log format.
            if not Utils.check_level_handler_exists(self.logger, log_level):
                # Create a stream handler.
                handler = logging.StreamHandler()

                # Set the log level to the handler.
                handler.setLevel(constants.LOG_LEVELS.get(log_level))

                # Add the handler to the logger.
                self.logger.addHandler(handler)

            # Create a formatter object.
            formatter = logging.Formatter(log_format)

            # TODO: Multiple handlers for the same log level could be present. Set the log format for each handler.
            # Currently, only one handler for a log level is present in the logger is assumed.
            # Get the handler for the log level.
            handler = Utils.get_level_handler(self.logger, log_level)

            # Set the formatter to the handler.
            handler.setFormatter(formatter)

    def single_file_logging(
        self, file_path: str = str(), log_level: str = "INFO"
    ) -> logging.Logger:
        """
        This function is used to create a logger object, which will direct the logs
        to the specified file with the specified log level. If no file path is provided,
        the logs will be directed to the default log directory with the name of the logger.

        Args:
            file_path (str): The file path to which the logs will be directed. DEFAULT: DEFAULT_LOG_DIR.
            log_level (str): The log level. DEFAULT: "INFO".
        Output:
            logger (logging.Logger): The logger object.
        """
        # Check if the log level is a valid log level, raise an error if not.
        if log_level not in constants.LOG_LEVELS:
            raise ValueError(f"Invalid log level: {log_level}")

        # If the file path is not provided, set the default file path.
        if not file_path:
            file_path = constants.DEFAULT_LOG_DIR.format(
                f"advanced_logger/{self.logger_name}.log"
            )

        # Get the directory path of the file path.
        directory_path = os.path.dirname(file_path)

        # Check if the directory exists. If not, create it.
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        # While a handler for a log level exists, close the handler.
        while Utils.check_level_handler_exists(self.logger, log_level):

            # Get the handler for the log level.
            handler = Utils.get_level_handler(self.logger, log_level)

            # Remove the handler from the logger.
            handler.close()

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

    def multi_file_logging(self, config: dict = dict()) -> logging.Logger:
        """
        This function is used to create a logger object, which will direct the logs
        to the specified file with the specified log level. If no file path is provided,
        the logs will be directed to the default log directory with the name of the logger.
        All the handlers for the log levels already present in the logger will be closed.

        Args:
            config (dict): The configuration dictionary for log level to file path. DEFAULT: dict().
        Output:
            logger (logging.Logger): The logger object.
        """

        # Loop through the configuration dictionary.
        for log_level, file_path in config.items():

            # Check if the log level is a valid log level, raise an error if not.
            if log_level not in constants.LOG_LEVELS:
                raise ValueError(f"Invalid log level: {log_level}")

            # If the file path is not provided, set the default file path.
            if not file_path:
                # Get the default file path for the log level.
                file_path = constants.DEFAULT_LOG_LEVEL_TO_FILE_PATH[log_level].format(
                    constants.DEFAULT_LOG_DIR.format(self.logger_name)
                )

            # Get the directory path of the file path.
            directory_path = os.path.dirname(file_path)

            # Check if the directory exists. If not, create it.
            if not os.path.exists(directory_path):
                os.makedirs(directory_path)

            # While a handler for a log level exists, close the handler.
            while Utils.check_level_handler_exists(self.logger, log_level):

                # Get the handler for the log level.
                handler = Utils.get_level_handler(self.logger, log_level)

                # Remove the handler from the logger.
                handler.close()

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
