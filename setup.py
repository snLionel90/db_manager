
import os
import setuptools

__author__="sn.lionel90"
print(__author__)

with open ("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'db_manager',
    version = '1.3.2020',
    author = 'sn.Lionel90 aka Lionel Sanchez',
    description = ("manage easily your database"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url = 'https://github.com/snLionel90/db_manager',
    keywords=['database_manager', 'snLionel90', 'db', 'database', 'MySQL'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: db_manager :: snLionel90 ",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    include_package_data=True,
)


