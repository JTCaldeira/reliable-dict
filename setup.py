import os
import sys

from setuptools import setup, find_packages


os.chdir(os.path.dirname(sys.argv[0]) or ".")

setup(
    name="reliable-dict",
    version="0.0.1",
    description="A dictionary implementation that attempts to achieve a better worst case complexity and use less memory than the standard dictionary.",
    long_description=open("README.md", "rt").read(),
    url="https://github.com/JTCaldeira/reliable-dict",
    author="João Caldeira",
    author_email="jt.caldeira@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: PyPy",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
	"Operating System :: OS Independent",
    ],
    packages=find_packages(),
    install_requires=["cffi>=1.0.0"],
    setup_requires=["cffi>=1.0.0"],
    cffi_modules=[
        "./cffi_example/build_person.py:ffi",
        "./cffi_example/build_fnmatch.py:ffi",
    ],
)
