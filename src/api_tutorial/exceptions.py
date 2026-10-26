"""This module contains custom exceptions for this project."""


class DuplicateSlugError(Exception):
    """Raised when a station with the same slug already exists."""
