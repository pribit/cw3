import logging
import os

from config import LOGS_DIRECTORY


def mk_log_directory():
    if not os.path.exists(LOGS_DIRECTORY):
        os.mkdir(LOGS_DIRECTORY)


def create_logger():
    logger = logging.getLogger('basic')
    logger.setLevel(logging.INFO)

    mk_log_directory()
    file_handler = logging.FileHandler(f'{LOGS_DIRECTORY}/log.log')
    logger.addHandler(file_handler)

    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    file_handler.setFormatter(formatter)

