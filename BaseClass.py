import logging


class BaseClass:
    def getLogger(self):
        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler('logfile.log')
        formatterr = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatterr)
        logger.setLevel(logging.INFO)
        logger.addHandler(fileHandler)
        return logger