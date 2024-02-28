"""
    This module contains the general logging functions. It can be used to log
    messages in a flask application ONLY.

    Author: Aaksh Ranjan
"""

import inspect
import logging
import uuid

from flask import Flask, request

from . import GeneralLogging, constants

class FlaskLogging(GeneralLogging):
    
    def __init__(self, logger_name: str) -> None:
        """
        This function is used to initialize the FlaskLogging object.

        Args:
            logger_name (str): The name of the logger.
        Output:
            NONE
        """
        super().__init__(logger_name)

    def config_unique_id(self, app: Flask) -> None:
        """
        This function is used to configure a unique request id for each request.

        Args:
            NONE
        Output:
            NONE
        """
        @app.before_request
        def before_request():
            request.request_id = str(uuid.uuid4())