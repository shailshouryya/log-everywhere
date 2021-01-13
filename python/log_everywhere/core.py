import sys
import datetime
import threading

import contextlib

NEWLINE = '\n'


@contextlib.contextmanager
def yield_logger(filepath, log_silently=False):
    '''
    Requires a string for the filepath argument and accepts an optional boolean for the log_silently argument.
    The provided filepath will be the location all messages will be logged to.

    If log_silently is not set or is set to False, all messages will ALSO be logged to the console.
    If log_silently is set to True, all messages will be logged to ONLY the filepath.
    '''
    filepath = filepath.strip('.log')
    log_file = f'{filepath}.log'
    with open (log_file, 'a', encoding='utf-8') as output_location:
        if log_silently is True: yield (output_location,)
        else:                    yield (output_location, sys.stdout)


def log(message, logging_locations):
    thread_name = threading.current_thread().name
    thread_name = f'[{threading.current_thread().name}]'
    isoformat   = datetime.datetime.isoformat
    now         = datetime.datetime.now
    message     = f'===>{thread_name:>>14} {isoformat(now())}: {message}\n'
    for location in logging_locations:
        location.writelines(message)
