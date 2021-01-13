'''
Logging package to enable writing the corresponding datetime
at which every logged event happenes to multiple, DIFFERENT files
safely when running multiple threads
(multi-threading with python standard library's `threading` package).
'''
from .core import yield_logger
from .core import log

'''
version:              0.0.0
author:               Shail-Shouryya
email:                shailshouryya@gmail.com
development_status:   4 - Beta
intended_audience:    Developers
license:              OSI Approved :: Apache License 2.0
ideal_python_version: Python 3.6+
source:               https://github.com/Shail-Shouryya/log-everywhere/python
'''


__version__              = '0.0.0'
__author__               = 'Shail-Shouryya'
__email__                = 'shailshouryya@gmail.com'
__development_status__   = '4 - Beta'
__intended_audience__    = 'Developers'
__license__              = 'OSI Approved :: Apache License 2.0'
__ideal_python_version__ = 'Python 3.6+'
__source__               = 'https://github.com/Shail-Shouryya/log-everywhere/python'
