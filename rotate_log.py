import time
import logging
from logging.handlers import RotatingFileHandler
from logging.handlers import TimedRotatingFileHandler

''' Rotating logs by time or by size '''

logger = logging.getLogger("rotation")
logger.setLevel(logging.INFO)

# s,m,h,d...   - (seconds,minutes,hours,days)and so one  Please read the docs
rotate_handler = RotatingFileHandler("logs/rotate.log",maxBytes=2000,backupCount=10)
timed_rotate_handler = TimedRotatingFileHandler("logs/rotate_time.log",when='s',interval=5,backupCount=10)

logger.addHandler(rotate_handler)
logger.addHandler(timed_rotate_handler)

for _ in range(10000):    
    logger.info("I am rotate logger")
for _ in range(6):
    logger.info("I am time log message")    
    time.sleep(6)