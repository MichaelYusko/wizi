"""File for helpers"""

import wiz.constants
from wiz.errors import LicenseError

DEFAULT_LICENCES = {
    'MIT': wiz.constants.MIT_LICENSE
}


def create_license_file(license_name: str) -> str:
    """"
    :param license_name: An license name
    :return: An content of license
    """
    license_content = DEFAULT_LICENCES.get(license_name)
    if license_content is None:
        raise LicenseError
    return license_content
