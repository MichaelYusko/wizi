"""Base generator file"""
import os
import sys


class BaseGenerator:  # pylint: disable=too-few-public-methods
    """Base generator class"""
    def __init__(self, project_name):
        self.project_name = project_name


class FileGenerator(BaseGenerator):  # pylint: disable=too-few-public-methods
    """Generator class for an file"""
    pass


class DirectoryGenerator(BaseGenerator):  # pylint: disable=too-few-public-methods
    """Generator class for an directory"""
    def __init__(self, project_name):  # pylint: disable=useless-super-delegation
        super().__init__(project_name)

    def _create_directory(self):
        """
        :return: Create an directory
        """
        if not os.path.isdir(self.project_name):
            os.mkdir(self.project_name)
            sys.exit(1)
        else:
            print('The {} project already exists'.format(self.project_name))
            sys.exit(1)
