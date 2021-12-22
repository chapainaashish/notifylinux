import setuptools

__author__ = "Aashish Sharma"
__license__ = "GPL-3.0"
__email__ = "ashishchapain86@gmail.com"

with open("README.md", "r") as rmd:
    long_description = rmd.read()

setuptools.setup(name="notifylinux",
                 version="0.0.8",
                 author="Aashish Sharma",
                 author_email="ashishchapain86@gmail.com",
                 description="A python package to send desktop notification in linux",
                 long_description=long_description,
                 url="https://github.com/aasis2520c/notifylinux",
                 packages=setuptools.find_packages(),
                 classifiers=[
                     "Programming Language :: Python :: 3",
                     "License :: GPL-3.0 license",
                     "Operating System :: Linux"
                 ]
                 )
