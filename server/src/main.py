import os
from logging import getLogger

from logging_conf import setup_logging
setup_logging()  # out of order because importing uvicorn and routes fires off logger events

from uvicorn import run

from routes import app

_logger = getLogger("main.main")


if __name__ == '__main__':
    _logger.info("Running uvicorn")
    run(app, log_config=None, host=os.getenv("host", default="127.0.0.1"))
