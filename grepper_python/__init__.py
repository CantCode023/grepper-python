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

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

import logging
from typing import NamedTuple, Literal

from .answer import GrepperAnswer
from .main import Grepper

logging.getLogger(__name__).addHandler(logging.NullHandler())

del (
    logging,
    NamedTuple,
    Literal,
)
