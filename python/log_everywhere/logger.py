import sys
import datetime
import threading

import contextlib


@contextlib.contextmanager
def yield_logger(filepath, log_silently=False):
    '''
    Requires a string for the filepath argument and accepts an optional boolean for the log_silently argument.
    Creates a file at the specified filepath (if it doesn't already exist) and appends all messages to this location.

    Logs all messages to the filepath AND console if log_silently is not set or is set to False.
    Logs all messages to the filepath ONLY if log_silently is set to True.
    '''
    filepath = filepath.strip('.log')
    log_file = f'{filepath}.log'
    with open (log_file, 'a', encoding='utf-8') as output_location:
        if log_silently is True: yield (output_location,)
        else:                    yield (output_location, sys.stdout)


def log(message, logging_locations, show_thread=True):
    '''
    Accepts a string for the message argument and the context manager object
    created with yield_logger as the logging_locations argument.

    Logs the provided message to every location in logging_locations.

    The logging_locations argument is an iterable of _io.TextIOWrapper objects.
    '''
    thread_name = ''
    if show_thread:
        thread_name = threading.current_thread().name
        thread_name = f'[{threading.current_thread().name}]'
    isoformat   = datetime.datetime.isoformat
    now         = datetime.datetime.now
    message     = f'===>{thread_name:>>14} {isoformat(now())}: {message}\n'
    for location in logging_locations:
        location.writelines(message)
