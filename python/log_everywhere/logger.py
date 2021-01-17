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


def log(message, logging_locations, show_thread=True, show_datetime=True, pad='===>'):
    '''
    Accepts a string for the message argument and the context manager object
    created with yield_logger as the logging_locations argument.
    Accepts a boolean for the show_thread and show_datetime arguments
    and a string for the pad argument.

    Logs the provided message to every location in logging_locations.

    The logging_locations argument is an iterable of _io.TextIOWrapper objects.

    Prepends thread name to all messages if show_thread is True (default).
    Prepends datetime    to all messages if show_datetime is True (default; added after the thread name if show_thread is also True).
    Prepends string provided to all messages if pad is specified, otherwise prepends all messages with: ===>
      ->> to prepend nothing, use: pad=''
    '''
    thread_name  = ''
    current_time = ''
    if show_thread:
        thread_name = f'[{threading.current_thread().name}]'
    if show_datetime:
        isoformat    = datetime.datetime.isoformat
        now          = datetime.datetime.now
        current_time = isoformat(now())
    # formatted_message keys are a tuple of (pad, show_thread, show_datetime)
    formatted_message = {
        (True,  True,  True):  f'{pad}{thread_name:>>14} {current_time}: {message}\n',
        (False, True,  True):  f'{thread_name:>>14} {current_time}: {message}\n',
        (True,  False, True):  f'{pad}{current_time}: {message}\n',
        (True,  True,  False): f'{pad}{thread_name:>>14} {message}\n',
        (False, False, True):  f'{current_time}: {message}\n',
        (False, True,  False): f'{thread_name:>>14} {message}\n',
        (True,  False, False): f'{pad} {message}\n',
        (False, False, False): f'{message}\n',
    }
    message = formatted_message[(not pad, show_thread, show_datetime)]
    for location in logging_locations:
        location.writelines(message)
