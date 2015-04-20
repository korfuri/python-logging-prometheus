import unittest
import logging
from prometheus_client import REGISTRY
import logging_prometheus


class TestLoggingPrometheus(unittest.TestCase):
    def test_rootLoggerExports(self):
        logging.error('There was an error.')

        self.assertEquals(
            1, REGISTRY.get_sample_value('python_logging_messages_total',
                                         labels={'logger': 'test_levels',
                                                 'level': 'ERROR'}))

    def test_all_levels(self):
        logger = logging.getLogger('test_levels')
        logger.setLevel(logging.DEBUG)
        logger.debug('debug message')
        logger.info('info message')
        logger.warn('warn message')
        logger.error('error message')
        logger.critical('critical message')
        for level in ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'):
            self.assertEquals(
                1, REGISTRY.get_sample_value('python_logging_messages_total',
                                             labels={'logger': 'test_levels',
                                                     'level': level}))

    def test_setLevel(self):
        logger = logging.getLogger('test_setLevel')
        logger.setLevel(logging.CRITICAL)
        logger.debug('debug message')
        logger.info('info message')
        logger.warn('warn message')
        logger.error('error message')
        logger.critical('critical message')
        for level in ('DEBUG', 'INFO', 'WARNING', 'ERROR'):
            self.assertEquals(
                None,
                REGISTRY.get_sample_value('python_logging_messages_total',
                                          labels={'logger': 'test_setLevel',
                                                  'level': level}))
        self.assertEquals(
            1, REGISTRY.get_sample_value('python_logging_messages_total',
                                         labels={'logger': 'test_levels',
                                                 'level': 'CRITICAL'}))


if __name__ == '__main__':
    unittest.main()
