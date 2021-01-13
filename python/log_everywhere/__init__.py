'''
Logging package to enable writing the corresponding datetime
at which every logged event happened to multiple, DIFFERENT files
safely when running multiple threads
(multi-threading with python standard library's `threading` package).
'''
from .core import yield_logger
from .core import log
