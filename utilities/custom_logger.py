import inspect
import logging


def customLogger(logLevel=logging.DEBUG):
    # Gets the name of the class / method from where this method is called
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    # file_handler = logging.FileHandler(filename='{0}.log'.format(logger_name), mode='w')
    # create one file and append the logs
    file_handler = logging.FileHandler(filename='automation.log', mode='a')
    file_handler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                      datefmt='%m/%d/%Y  %H:%M:%S')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
