"""Base generator file"""
import abc
import os
import sys

from .helpers import write_license_file


class BaseGenerator:  # pylint: disable=too-few-public-methods
    """Base generator class"""
    def __init__(self, project_name):
        self.project_name = project_name

    @abc.abstractmethod
    def create(self):
        """Abstract method for all child classes"""
        pass

    def _make_path(self, file_name):
        """
        :param file_name: An file name
        :return: Path where, files would be saved
        """
        path = os.getcwd()
        return '{}/{}/{}'.format(path, self.project_name, file_name)


class FileGenerator(BaseGenerator):  # pylint: disable=too-few-public-methods
    """Generator class for an file"""
    def __init__(self, project_name):  # pylint: disable=useless-super-delegation
        super().__init__(project_name)

    _default_files = [
        'requirements.txt', '.travis.yml',
        'setup.py', 'tox.ini', 'LICENSE',
        'README.md', '.gitignore'
    ]

    def create_files(self, license_type, author_name):
        """
        Create an files,in the root directory of project
        and write License context, with an author name
        """
        for file_name in self._default_files:
            with open(self._make_path(file_name), 'w') as file:
                file.write('# Wizi project')

        with open(self._make_path('LICENSE'), 'w') as file:
            write_license = write_license_file(license_type, author_name)
            file.write(write_license)


class DirectoryGenerator(BaseGenerator):  # pylint: disable=too-few-public-methods
    """Generator class for an directory"""
    def __init__(self, project_name):  # pylint: disable=useless-super-delegation
        super().__init__(project_name)

    def create(self):
        """Create an directory"""
        if os.path.isdir(self.project_name):
            print('The {} project already exists'.format(self.project_name))
            sys.exit(1)
        else:
            os.mkdir(self.project_name)


class WiziGenerator:  # pylint: disable=too-few-public-methods
    """Main class for generate flow"""
    def __init__(self, project_name):
        self.directory = DirectoryGenerator(project_name)
        self.files = FileGenerator(project_name)

    def create_project(self, license_type, author_name):
        """Start an project"""
        self.directory.create()
        self.files.create_files(license_type, author_name)
