#!/usr/bin/env python3
"""
Setup configuration for the Hello World application.
"""
from setuptools import setup, find_packages

setup(
    name="mbtest-hello-world",
    version="1.0.0",
    description="A simple Hello World Python application",
    author="mbtest",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "hello-world=main:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
