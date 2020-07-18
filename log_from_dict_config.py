import logging
from logging.config import dictConfig
from config.config import  log_config
logging.config.dictConfig(log_config)
logger = logging.getLogger("myapp")

logger.warning("Show me on console")
logger.info("i would prefer write to a file")

