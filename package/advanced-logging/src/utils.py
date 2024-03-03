"""
    This module contains utility functions class for the advanced-logging package.

    Author: Aaksh Ranjan
"""

import inspect
import logging
import constants

from typing import Tuple, Union

class Utils:

    @staticmethod
    def check_level_handler_exists(logger: logging.Logger, level: Union[str, int]) -> bool:
        """
        This function is used to check if a handler for a particular log level exists.

        Args:
            logger (logging.Logger): The logger object.
            level (Union[str, int]): The log level.
        Output:
            bool: True if the handler exists, False otherwise.
        """

        # If the level is a string, convert it to the corresponding integer.
        if isinstance(level, str):
            level = constants.LOG_LEVELS.get(level.upper(), None)

        # If the level is not found, return False.
        if level is None:
            return False

        # Iterate through the handlers of the logger.
        for handler in logger.handlers:
            # If the level of the handler is the same as the level provided, return True.
            if handler.level == level:
                return True

        # If no handler is found, return False.
        return False
    
    @staticmethod
    def get_level_handler(logger: logging.Logger, level: Union[str, int]) -> Union[None, logging.Handler]:
        """
        This function is used to get the handler for a particular log level.

        Args:
            logger (logging.Logger): The logger object.
            level (Union[str, int]): The log level.
        Output:
            Union[None, logging.Handler]: The handler if found, None otherwise.
        """

        # If the level is a string, convert it to the corresponding integer.
        if isinstance(level, str):
            level = constants.LOG_LEVELS.get(level.upper(), None)

        # If the level is not found, return False.
        if level is None:
            return None

        # Iterate through the handlers of the logger.
        for handler in logger.handlers:
            # If the level of the handler is the same as the level provided, return True and the handler.
            if handler.level == level:
                return handler

        # If no handler is found, return False and None.
        return None