from setuptools import setup, find_packages
import os

setup_packages = [f"gender_recognition.{package}" for package in find_packages(where=os.path.join(os.path.dirname(__file__), 'src'))]
setup_packages.append("gender_recognition")

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    requirements = [line.strip() for line in f.read().splitlines()]

setup(
    name='gender_recognition',
    version="1.3",
    packages=setup_packages,
    include_package_data=True,
    package_dir={"gender_recognition": "src"},
    url='https://github.com/javibg96/gender_recognition/',
    author='Javier Blasco',
    install_requires=requirements,
    author_email="blascogarcia.javier@outlook.com",
    description=' '
)
