# https://pypi.org/classifiers/
# https://test.pypi.org/pypi?%3Aaction=list_classifiers
# https://github.com/pypa/sampleproject/blob/master/setup.py
# https://packaging.python.org/guides/distributing-packages-using-setuptools/
from setuptools import setup, find_packages


with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name                          = 'log_everywhere',
    version                       = '0.0.0',
    description                   = 'Logging package to enable writing all program information with corresponding datetime to multiple, DIFFERENT files safely when running multiple threads (multi-threading).',
    long_description              = long_description,
    long_description_content_type = 'text/markdown',
    url                           = 'https://github.com/Shail-Shouryya/log_everywhere',
    author                        = 'Shail-Shouryya',
    author_email                  = 'yt.videos.list@gmail.com',
    license                       = 'Apache License 2.0',


    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: Free for non-commercial use',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Internet :: Log Analysis',
        'Topic :: System :: Logging',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Environment :: Plugins',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: Mozilla',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Customer Service',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Legal Industry',
        'Intended Audience :: Manufacturing',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft',
        'Operating System :: Microsoft :: MS-DOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: OS Independent',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: AIX',
        'Operating System :: POSIX :: BSD',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Communications',
        'Topic :: Communications :: BBS',
        'Topic :: Communications :: Chat',
        'Topic :: Communications :: Chat :: Unix Talk',
        'Topic :: Communications :: Conferencing',
        'Topic :: Communications :: Email',
        'Topic :: Communications :: File Sharing',
        'Topic :: Database',
        'Topic :: Database :: Front-Ends',
        'Topic :: Documentation',
        'Topic :: Education :: Testing',
        'Topic :: Home Automation',
        'Topic :: Internet',
        'Topic :: Internet :: File Transfer Protocol (FTP)',
        'Topic :: Internet :: Finger',
        'Topic :: Internet :: Name Service (DNS)',
        'Topic :: Internet :: Proxy Servers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Browsers',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Content Management System',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Page Counters',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Internet :: WWW/HTTP :: Session',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Internet :: WWW/HTTP :: Site Management :: Link Checking',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
        'Topic :: Multimedia',
        'Topic :: Multimedia :: Graphics :: 3D Modeling',
        'Topic :: Multimedia :: Graphics :: 3D Rendering',
        'Topic :: Multimedia :: Graphics :: Capture',
        'Topic :: Multimedia :: Graphics :: Capture :: Digital Camera',
        'Topic :: Multimedia :: Graphics :: Capture :: Scanners',
        'Topic :: Multimedia :: Graphics :: Capture :: Screen Capture',
        'Topic :: Multimedia :: Graphics :: Presentation',
        'Topic :: Multimedia :: Graphics :: Viewers',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Multimedia :: Sound/Audio :: Analysis',
        'Topic :: Multimedia :: Sound/Audio :: Capture/Recording',
        'Topic :: Multimedia :: Sound/Audio :: Conversion',
        'Topic :: Multimedia :: Sound/Audio :: Sound Synthesis',
        'Topic :: Multimedia :: Sound/Audio :: Speech',
        'Topic :: Multimedia :: Video :: Capture',
        'Topic :: Office/Business',
        'Topic :: Office/Business :: Financial',
        'Topic :: Office/Business :: Financial :: Accounting',
        'Topic :: Office/Business :: Financial :: Investment',
        'Topic :: Office/Business :: Financial :: Point-Of-Sale',
        'Topic :: Office/Business :: Financial :: Spreadsheet',
        'Topic :: Office/Business :: Groupware',
        'Topic :: Office/Business :: News/Diary',
        'Topic :: Office/Business :: Scheduling',
        'Topic :: Printing',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development',
        'Topic :: Software Development :: Bug Tracking',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Debuggers',
        'Topic :: Software Development :: Documentation',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Localization',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Testing :: Acceptance',
        'Topic :: Software Development :: Testing :: Mocking',
        'Topic :: Software Development :: Testing :: Traffic Generation',
        'Topic :: Software Development :: Testing :: Unit',
        'Topic :: Software Development :: Version Control :: Git',
        'Topic :: System',
        'Topic :: System :: Archiving',
        'Topic :: System :: Archiving :: Backup',
        'Topic :: System :: Benchmark',
        'Topic :: System :: Boot',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Filesystems',
        'Topic :: System :: Hardware :: Symmetric Multi-processing',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Networking',
        'Topic :: System :: Networking :: Firewalls',
        'Topic :: System :: Networking :: Monitoring',
        'Topic :: System :: Networking :: Monitoring :: Hardware Watchdog',
        'Topic :: System :: Networking :: Time Synchronization',
        'Topic :: System :: Operating System',
        'Topic :: System :: Recovery Tools',
        'Topic :: System :: Shells',
        'Topic :: System :: Software Distribution',
        'Topic :: System :: System Shells',
        'Topic :: System :: Systems Administration',
        'Topic :: Text Editors :: Documentation',
        'Topic :: Text Editors :: Text Processing',
        'Topic :: Text Editors :: Word Processors',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Fonts',
        'Topic :: Text Processing :: General',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Text Processing :: Markup',
        'Topic :: Text Processing :: Markup :: HTML',
        'Topic :: Utilities'
    ],
    keywords='logging logger threading multi-threading datetime time archiving tracing debugging tracer debugger automation csv txt markdown md YouTube videos URL scraping Selenium macos windows linux',


    # http://code.nabla.net/doc/setuptools/api/setuptools/setuptools.find_packages.html
    # https://stackoverflow.com/questions/51286928/what-is-where-argument-for-in-setuptools-find-packages
    packages=find_packages(exclude=['*dev*']),
    # packages=find_namespace_packages(include=['ship']),
    # package_dir={'':'src'},


    python_requires  = '>=3.6.*, <4',
    install_requires = [],  # Optional
    # https://packaging.python.org/discussions/install-requires-vs-requirements/


    # If there are data files included in your packages that need to be installed, specify them here.
    # If using Python 2.6 or earlier, then these have to be included in MANIFEST.in as well.
    package_data = {  # Optional
        # 'sample': ['package_data.dat'],
    },
    # Although 'package_data' is the preferred approach, in some case you may need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],  # Optional


    # To provide executable scripts, use entry points in preference to the "scripts" keyword.
    # Entry points provide cross-platform support and allow `pip` to create the appropriate form of executable for the target platform.
    # For example, the following would provide a command called `log_everywhere` which executes the code in the module `__main__` from this package when invoked directly from the command line:
    # entry_points={  # Optional
    #    'console_scripts': [
    #        'log_everywhere=log_everywhere:__main__',
    #    ],
    # },


    project_urls = {
        'Bug Reports':   'https://github.com/Shail-Shouryya/log_everywhere/issues',
        'PyPi Funding':  'https://donate.pypi.org',
        'Source':        'https://github.com/Shail-Shouryya/log_everywhere',
        'Pull requests': 'https://github.com/Shail-Shouryya/log_everywhere/pulls',
        'Issues':        'https://github.com/Shail-Shouryya/log_everywhere/issues',
        'Code':          'https://github.com/Shail-Shouryya/log_everywhere/tree/main/python'
    },
)
