"""
Python Grepper API
~~~~~~~~~~~~~~~~~~~
An API wrapper for the Grepper API.
"""

__title__ = "grepper-python"
__author__ = "CodeGrepper"
__license__ = "MIT"
__copyright__ = "Copyright 2010-2023 Grepper, Inc."
__version__ = "0.0.1a"

from grepper_python.answer import GrepperAnswer
from grepper_python.main import Grepper
from grepper_python.exceptions import BadRequest
from grepper_python.exceptions import Unauthorized
from grepper_python.exceptions import Forbidden
from grepper_python.exceptions import NotFound
from grepper_python.exceptions import MethodNotAllowed
from grepper_python.exceptions import TooManyRequests
from grepper_python.exceptions import InternalServerError
from grepper_python.exceptions import ServiceUnavailable

__all__ = ["GrepperAnswer", "Grepper", "BadRequest", "Unauthorized", "Forbidden", "NotFound", "MethodNotAllowed", "TooManyRequests", "InternalServerError", "ServiceUnavailable"]