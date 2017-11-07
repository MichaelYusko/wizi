"""Setup file"""

from distutils.core import setup

import wiz

VERSION = wiz.__version__
AUTHOR = wiz.__author__

setup_kwargs = {
    'name': 'wizi',
    'version': VERSION,
    'url': 'https://github.com/MichaelYusko/wizi',
    'license': 'MIT',
    'author': AUTHOR,
    'author_email': 'freshjelly12@yahoo.com',
    'description': 'Fast template generator for your project',
    'packages': ['wiz'],
    'classifiers': [
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License'
    ],
 }

requirements = ['click==6.7']
setup_kwargs['install_requires'] = requirements
setup(**setup_kwargs)

print(u"\n\n\t\t    "
      "Wizi version {} installation succeeded.\n".format(VERSION))
