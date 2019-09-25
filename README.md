# python-logging-prometheus
Export metrics about your Python application's logging volume for Prometheus.io.

[![PyPI version](https://badge.fury.io/py/logging-prometheus.svg)](http://badge.fury.io/py/logging-prometheus)
[![Build Status](https://travis-ci.org/korfuri/python-logging-prometheus.svg?branch=master)](https://travis-ci.org/korfuri/python-logging-prometheus)
[![PyPi page link -- Python versions](https://img.shields.io/pypi/pyversions/python-logging-prometheus.svg)](https://pypi.python.org/pypi/python-logging-prometheus)


## Installation

```shell
pip install logging_prometheus
```

## Usage

Simply `import logging_prometheus` to register the metrics.

See the prometheus_client
[documentation](https://github.com/prometheus/client_python) to see
how to export the metrics via an HTTP server. If you're using Django,
check out
[django-prometheus](https://github.com/korfuri/django-prometheus)
which can export metrics to a Django view, and exports metrics
relevant to Django.

To aggregate the exported variables, see the [Prometheus.io documentation](http://prometheus.io/).
