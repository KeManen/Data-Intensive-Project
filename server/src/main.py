from logging import getLogger

from application import application
from logging_conf import setup_logging

app = application
setup_logging()
_logger = getLogger("main.main")


@app.get("/")
async def root():
    _logger.debug("Root called")
