#!/usr/bin/env python3
from setuptools import setup, find_packages

version = '0.0.1'

setup(
    name="alerta-reject-duplicate",
    version=version,
    description='Example Alerta plugin for droping duplicate alerts',
    url='https://github.com/alerta/alerta-contrib',
    license='Apache License 2.0',
    author='Brian Goldberg',
    author_email='bgoldberg@fake-company.com',
    packages=find_packages(),
    py_modules=['alerta_reject_duplicate'],
    install_requires=[],
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'alerta.plugins': [
            'reject_duplicate = alerta_reject_duplicate:RejectDuplicate'
        ]
    }
)
