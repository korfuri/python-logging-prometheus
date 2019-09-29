import os
from setuptools import setup

LONG_DESCRIPTION = """Logging-Prometheus

Exports metrics about the logging of your Python application for
Prometheus.io.

See https://github.com/korfuri/python-logging-prometheus for usage
instructions.
"""

setup(
    name="logging-prometheus",
    version="0.1.0",
    author="Uriel Corfa",
    author_email="uriel@corfa.fr",
    description=(
        "Exports logging metrics for Prometheus.io."),
    license="Apache",
    keywords="python logging monitoring prometheus",
    url="http://github.com/korfuri/python-logging-prometheus",
    packages=["logging_prometheus"],
    test_suite="tests",
    long_description=LONG_DESCRIPTION,
    install_requires=[
        "prometheus_client>=0.0.8",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Topic :: System :: Monitoring",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
    ],
)
