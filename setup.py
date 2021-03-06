from setuptools import setup, find_packages
import os, sys

    # Which directory is this file's parent?
parent_directory = os.path.abspath(os.path.dirname(__file__))

dependancies = [
    'pyramid',
    'repoze.tm2>=1.0b1',
    'WebError',
    'sqlalchemy',
    'zope.sqlalchemy',
    'elixir',
]

meta_files = {
    'README.md': None,
    'CHANGES.md': None,
    'CLASSIFIERS.txt': None,
    'ENTRY_POINTS.ini': None,
}

# The following bit will read each index from meta_files and fill it's value
# with the contents of that file if it is able to read the file.
for filename in meta_files:
    try:
        current_file = open(os.path.join(parent_directory, filename))
        meta_files[filename] = current_file.read()
        current_file.close()
    except IOError:
        pass

setup(name = 'Vaktuk',
      version = '0.0.0',
      description = 'Content management in Pyramid',
      long_description = meta_files['README.md'] + '\n\n' + meta_files['CHANGES.md'],
      classifiers = meta_files['CLASSIFIERS.txt'],
      author = 'Brandon R. Stoner',
      author_email = 'monokrome@limpidtech.com',
      url = 'http://vatuk.limpidtech.com/',
      keywords = 'web pylons pyramid',
      packages = find_packages(),
      include_package_data = True,
      zip_safe = False,
      install_requires = dependancies,
      tests_require = dependancies,
      test_suite = 'vaktuk',
      entry_points = meta_files['ENTRY_POINTS.ini'],
      paster_plugins = [
        'pyramid',
      ],
)
