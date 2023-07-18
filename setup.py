# -*- coding: utf-8 -*-
from __future__ import annotations

from setuptools import find_packages
from setuptools import setup


setup(
    name="pump_offline_calibration_plugin",
    version="1.0.1",
    license="MIT",
    description="Perform an offline calibration of pumps.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author_email="christian.macdonald@ucsf.edu",
    author="Chris Macdonald",
    url="https://github.com/odcambc/pump_offline_calibration_plugin",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "pioreactor.plugins": "pump_offline_calibration_plugin = pump_offline_calibration_plugin"
    },
)
