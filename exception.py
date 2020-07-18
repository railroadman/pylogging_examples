import logging
import traceback
logger = logging.getLogger("exception")
try:
    a = [1,2,3]
    val = a[4]
except:
    logger.error("This is an error %s",traceback.format_exc())