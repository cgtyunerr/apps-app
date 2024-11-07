"""Common exceptions."""


class InvalidInputError(ValueError):
    """Invalid input."""


class NotFoundError(ValueError):
    """Not found."""


class ConflictError(ValueError):
    """Item conflict"""


class UnprocessableEntityError(ValueError):
    """Item is unprocessable."""


class ForbiddenError(ValueError):
    """Raise when user doesn't have any permission for given entity with the token."""
