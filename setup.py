from setuptools import setup, find_packages

setup(
    name="syntdatafft",
    version="0.1",
    packages=find_packages(),
    install_requires=["PySimpleGUI", "numpy", "matplotlib", "pytest"],
)
