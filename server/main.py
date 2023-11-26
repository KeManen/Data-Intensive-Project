from logging import getLogger

from logging_conf import setup_logging

if __name__ == '__main__':
    setup_logging()
    _logger = getLogger("main")
    _logger.info("Hello world")
