"""
grepper-python.exceptions
~~~~~~~~~~~~~~~~~~~
This module contains the set of grepper-python's exceptions.
"""

class GrepperDefaultException(Exception):
    def __init__(self, msg=None, *args, **kwargs):
        super().__init__(msg or self.__doc__, *args, **kwargs)

# 400
class BadRequest(GrepperDefaultException):
    """Your request is invalid."""


# 401
class Unauthorized(GrepperDefaultException):
    """Your API key is wrong."""


# 403
class Forbidden(GrepperDefaultException):
    """You do not have access to the requested resource."""


# 404
class NotFound(GrepperDefaultException):
    """The specified enpoint could not be found."""


# 405
class MethodNotAllowed(GrepperDefaultException):
    """You tried to access an enpoint with an invalid method."""


# 429
class TooManyRequests(GrepperDefaultException):
    """You're making too many requests! Slow down!"""


# 500
class InternalServerError(GrepperDefaultException):
    """We had a problem with our server. Try again later."""


# 503
class ServiceUnavailable(GrepperDefaultException):
    """We're temporarily offline for maintenance. Please try again later."""
