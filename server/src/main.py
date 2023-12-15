import os
from logging import getLogger

from uvicorn import run

from logging_conf import setup_logging
from routes import app


if __name__ == '__main__':
    setup_logging()
    _logger = getLogger("main.main")
    _logger.info("Running uvicorn")
    run(app, log_config=None, host=os.getenv("host", default="127.0.0.1"))
