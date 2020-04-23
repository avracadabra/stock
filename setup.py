#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup script for bulk-management"""

import os

from setuptools import find_packages, setup

version = "0.1.0"
here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.rst"), "r", encoding="utf-8") as readme_file:
    readme = readme_file.read()

with open(os.path.join(here, "CHANGELOG.rst"), "r", encoding="utf-8") as changelog_file:
    changelog = changelog_file.read()

requirements = [
    "sqlalchemy",
    "anyblok",
    "psycopg2-binary",
    "anyblok_pyramid",
    "gunicorn",
    "anyblok_marshmallow",
    "anyblok-wms-base",
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name="bulk_management",
    version=version,
    description="This project will provide bloks that add provide HTTP interfaces to AWB.",
    long_description=readme + "\n\n" + changelog,
    author="Pierre Verkest",
    author_email="pierreverkest84@gmail.com",
    url="https://github.com/petrus-v/bulk-management",
    packages=find_packages(),
    entry_points={"bloks": ["awb_http=bulk_management.awb_http:Awb_http"]},
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords="bulk-management",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    test_suite="tests",
    tests_require=test_requirements,
)
