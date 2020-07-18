import logging
from pythonjsonlogger import jsonlogger

logger = logging.getLogger("jsonlogger")
logger.setLevel(logging.DEBUG)
logHandler = logging.StreamHandler()

formatter = jsonlogger.JsonFormatter('%(asctime)s:%(levelname):%(name)s:%(message)s')
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)




def main():
    logger.info("json logs")
    logger.warning(" i am json logger")


if __name__ == '__main__':
    main()