"""File for helpers"""

import wiz.constants
from wiz.errors import LicenseError

DEFAULT_LICENCES = {
    'MIT': wiz.constants.MIT_LICENSE,
    'BSD': wiz.constants.BSD_LICENSE
}


def write_license_file(license_type: str, author_name=None) -> str:
    """"
    :param license_name: An license name
    :param author_name: An author name, will added in an license file
    :return: An content of license
    """
    license_content = DEFAULT_LICENCES.get(license_type)
    if license_content is None:
        raise LicenseError

    author_name = author_name if author_name else 'Change me!'
    out_put_license = license_content.replace('Wizi Generator', author_name)
    return out_put_license
