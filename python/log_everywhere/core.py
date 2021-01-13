import sys
import datetime
import threading

NEWLINE = '\n'


@contextlib.contextmanager
def yield_logger(file_name, log_silently):
    log_file = f'{file_name}.log'
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
