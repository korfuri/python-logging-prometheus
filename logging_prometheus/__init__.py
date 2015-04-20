import prometheus_client
import logging


log_entries = prometheus_client.Counter(
    'python_logging_messages_total',
    'Count of log entries by logger and level.',
    ['logger', 'level'])


class ExportingLogHandler(logging.Handler):
    """A LogHandler that exports logging metrics for Prometheus.io."""
    def emit(self, record):
        log_entries.labels(record.name, record.levelname).inc()


def export_stats_on_root_logger():
    """Attaches an ExportingLogHandler to the root logger.

    This should be sufficient to get metrics about all logging in a
    Python application, unless a part of the application defines its
    own logger and sets this logger's `propagate` attribute to
    False. The `propagate` attribute is True by default, which means
    that by default all loggers propagate all their logged messages to
    the root logger.
    """
    logger = logging.getLogger()
    logger.addHandler(ExportingLogHandler())


# Just importing this module should make us export the metrics for the
# root logger.
export_stats_on_root_logger()
