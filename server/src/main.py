from logging import getLogger

from uvicorn import run

from application import application
from logging_conf import setup_logging

setup_logging()
app = application
_logger = getLogger("main.main")


@app.get("/")
async def root():
    _logger.debug("Root called")


if __name__ == '__main__':
    run(app, log_config=None)
