'''
Logging package to enable writing the corresponding datetime
and thread on which every logged event happenes to
multiple, DIFFERENT files safely when running multiple threads
(multi-threading with python standard library's `threading` package).

🌟 Star 🌟 this repo on GitHub if you found it useful!
https://github.com/Shail-Shouryya/log-everywhere
'''
from .logger import yield_logger
from .logger import log


__version__              = '0.0.1'
__author__               = 'Shail-Shouryya'
__email__                = 'shailshouryya@gmail.com'
__development_status__   = '4 - Beta'
__intended_audience__    = 'Developers'
__license__              = 'OSI Approved :: Apache License 2.0'
__ideal_python_version__ = 'Python 3.6+'
__source__               = 'https://github.com/Shail-Shouryya/log-everywhere/python'
