import inspect
import logging
from datetime import datetime
import pytest


def generate_email():
    return "arsen+%s-%d@getaloecare.com" % (datetime.now().strftime("%Y-%m-%d"), datetime.now().timestamp())


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getlogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        filehandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger
