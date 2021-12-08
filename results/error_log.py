"""Log file for calculation errors"""

import logging

def log_errors(path, record_number):
    path = path.split('/')
    file_name = path[len(path) - 1]
    message = file_name + '' + str(record_number)
    logging.info(message)
