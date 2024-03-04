"""
grepper-python.exceptions
~~~~~~~~~~~~~~~~~~~
This module contains the set of grepper-python's exceptions.
"""

class DocDefaultException(Exception):
    def __init__(self, msg:str=None, *args, **kwargs):
        super().__init__(msg or self.__doc__, *args, **kwargs)

# 400
class BadRequest(DocDefaultException):
    """Your request is invalid."""


# 401
class Unauthorized(DocDefaultException):
    """Your API key is wrong."""


# 403
class Forbidden(DocDefaultException):
    """You do not have access to the requested resource."""


# 404
class NotFound(DocDefaultException):
    """The specified enpoint could not be found."""


# 405
class MethodNotAllowed(DocDefaultException):
    """You tried to access an enpoint with an invalid method."""


# 429
class TooManyRequests(DocDefaultException):
    """You're making too many requests! Slow down!"""


# 500
class InternalServerError(DocDefaultException):
    """We had a problem with our server. Try again later."""


# 503
class ServiceUnavailable(DocDefaultException):
    """We're temporarily offline for maintenance. Please try again later."""
