from setuptools import setup, find_packages
import os

# Read the version from __version__.py in the root directory
version_file = os.path.join(os.path.dirname(__file__), '__version__.py')
version_dict = {}
with open(version_file, 'r') as f:
    exec(f.read(), version_dict)
version = version_dict['version']

setup(
    name='iit',
    version=version,
    description='Image In Terminal',
    author='cumulus13',
    author_email='cumulus13@gmail.com',
    packages=find_packages(),
    py_modules=['iit'],
    install_requires=[
        'rich', 
    	'Pillow',
    	'requests',
    	'argparse',
    	'rich_argparse',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
