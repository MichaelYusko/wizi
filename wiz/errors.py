"""File error classes"""


class LicenseError(Exception):
    """Class for license errors"""
    def __str__(self):
        return 'License not found'
