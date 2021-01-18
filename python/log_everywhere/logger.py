'''
Import module with:
```
from log_everywhere import yield_logger
from log_everywhere import log
```
'''
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
    Logs all messages to ONLY the filepath if log_silently is set to True.
    '''
    filepath = filepath.strip('.log')
    log_file = f'{filepath}.log'
    with open (log_file, 'a', encoding='utf-8') as output_location:
        if log_silently is True: yield (output_location,)
        else:                    yield (output_location, sys.stdout)


def log(message, logging_locations, show_thread=True, show_datetime=True, pad='    '):
    '''
    Accepts a string for the message argument and the context manager object
    created with yield_logger as the logging_locations argument.
    Accepts a boolean for the show_thread and show_datetime arguments
    and a string for the pad argument.

    Logs the provided message to every location in logging_locations.

    The logging_locations argument is an iterable of _io.TextIOWrapper objects.

    Prepends thread name to all messages if show_thread is True (DEFAULT).
    Prepends datetime    to all messages if show_datetime is True (DEFAULT; added after the thread name if show_thread is also True).
    Prepends string provided to the pad argument to all messages if pad is specified, otherwise prepends all messages with 4 spaces.
      ->> to prepend nothing, use: pad=''

    Some usage examples:

    To log information and messages to both the log file and the console:

    ```
    with yield_logger('name_of_my_log_file') as locations:
        log('An important message', locations)
    ```

    To log information and messages to only the log file and mute logging to the console:

    ```
    with yield_logger('name_of_my_log_file', log_silently=True) as locations:
        log('An important message', locations)
    ```

    To log only messages and no information to the log file and the console:

    ```
    with yield_logger('name_of_my_log_file') as locations:
        log('An important message', locations, show_thread=False, show_datetime=False, pad='')
    ```

    To log only messages and no information to the log file and mute logging to the console:

    ```
    with yield_logger('name_of_my_log_file', log_silently=True) as locations:
        log('An important message', locations, show_thread=False, show_datetime=False, pad='')
    ```
    '''
    thread_name  = ''
    current_time = ''
    if show_thread:
        thread_name = f'[{threading.current_thread().name}]' + ' '
        thread_name = f'{thread_name:>15}'
    if show_datetime:
        current_time = datetime.datetime.now().isoformat() + ' '
    message = f'{pad}{thread_name}{current_time}{message}\n'
    for location in logging_locations:
        location.writelines(message)
