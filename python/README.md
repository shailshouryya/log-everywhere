# log-everywhere Python API

<p align="center">
  <a href="https://github.com/Shail-Shouryya/log-everywhere/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/Shail-Shouryya/log-everywhere?color=yellow&labelColor=black"></a>
  <a href="https://docs.python.org/3/index.html">    <img src="https://img.shields.io/badge/python-3.6%2B-blue?labelColor=black"/></a>
  <a href="https://www.python.org/dev/peps/pep-0008"><img src="https://img.shields.io/badge/code%20style-PEP8-yellow.svg?labelColor=black"/></a>
  <a href="https://github.com/Shail-Shouryya/log-everywhere/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/Shail-Shouryya/log-everywhere?color=blue&labelColor=black"></a>
  <a href="https://github.com/Shail-Shouryya/log-everywhere/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/Shail-Shouryya/log-everywhere?color=yellow&labelColor=black"></a>
  <br>
  <a href="https://badge.fury.io/py/log-everywhere"><img src="https://badge.fury.io/py/log-everywhere.svg" alt="PyPI version" height="20"></a>
  <br>
  <a href="https://pypi.org/project/log-everywhere/"><img alt="PyPI - Wheel" src="https://img.shields.io/pypi/wheel/log-everywhere?labelColor=black&label=PyPI%20-%20Wheel"></a>
  <a href="https://pypi.org/project/log-everywhere/#files/"><img alt="PyPI - Format" src="https://img.shields.io/pypi/format/log-everywhere?labelColor=black&label=PyPI%20-%20Format"></a>
  <a href="https://pypi.org/project/log-everywhere/#history/"><img alt="PyPI - Status" src="https://img.shields.io/pypi/status/log-everywhere?labelColor=black&label=PyPI%20-%20Status"></a>
  <br>
  <a href="https://pypi.org/project/log-everywhere/"><img alt="PyPI - Implementation" src="https://img.shields.io/pypi/implementation/log-everywhere?labelColor=black&label=PyPI%20-%20Implementation"></a>
  <a href="https://pypi.org/project/log-everywhere/"><img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/log-everywhere?labelColor=black&label=PyPI%20-%20Python%20Version"></a>
  <br>
  <a href="https://codebeat.co/projects/github-com-shail-shouryya-log-everywhere-main"><img src="https://codebeat.co/badges/46b103ed-da79-4893-96af-ce95c9149532" alt="codebeat badge"/></a>
</p>

<details>
  <summary><b>Installing the package</b></summary>

Enter the following in your command line:

```python
# if something isn't working properly, try rerunning this
# the problem may have been fixed with a newer version

pip3 install -U log-everywhere     # MacOS/Linux
pip  install -U log-everywhere     # Windows
```
</details>

<details>
  <summary><b>Using the <code>log-everywhere</code> package</b></summary>

```
python3     # MacOS/Linux
python      # Windows
```
```python
from log_everywhere import yield_logger
from log_everywhere import log

def do_important_things(log_locations):
    num = 1 + 1
    log(f'This function calculated num to be: {num}', log_locations)
    product = num * 2
    log(f'This function calculated the product of num multiplied by 2 to be: {product}', log_locations)
    log( 'This function is now closing...', log_locations)

def main():
    with yield_logger('name_of_my_log_file', log_silently=False) as log_locations:
        log('>' * 50 + 'STARTING PROGRAM' + '<' * 50, log_locations)
        do_important_things(log_locations)
        log('>' * 50 + 'PROGRAM COMPLETE' + '<' * 50, log_locations)

main()
```
To see why [Python Standard Library](https://docs.python.org/3/library/)'s [logging](https://docs.python.org/3/library/logging.html) module was insufficient and creating a custom logger was necessary, [see this modification in the `yt-videos-list` package](https://github.com/Shail-Shouryya/yt-videos-list/commit/82a0129d82ea67475af902cf4a8a07c016d853b4). NOTE that the exact implementation differed slighlty in this commit (`yield_logger()` was named `yield_file_writer()`), and support for logging to both the console AND the log file [wasn't added until this commit](https://github.com/Shail-Shouryya/yt-videos-list/commit/fb8311869e89179dcf2bbf2849edcd5f97b216a1)

Direct link to commits:
  - [Simplify logging via custom context manager text writer](https://github.com/Shail-Shouryya/yt-videos-list/commit/82a0129d82ea67475af902cf4a8a07c016d853b4)
  - [Always log to log file but allow console logging muting](https://github.com/Shail-Shouryya/yt-videos-list/commit/fb8311869e89179dcf2bbf2849edcd5f97b216a1)

To see more interesting logging modifications, see the **significantly improves logging** section nested within the **details** section of the `yt-videos-list` package [0.5.0 Release](https://github.com/Shail-Shouryya/yt-videos-list/releases/tag/v0.5.0) page!
</details>

<details>
  <summary><b>Seeing <b>all</b> available functions for the <code>log-everywhere</code> package</b></summary>

```
python3     # MacOS/Linux
python      # Windows
```
```python
import log_everywhere
help(log_everywhere.logger)

# OR

from log_everywhere import logger
help(logger)

# SEEING PACKAGE METADATA
import log_everywhere
help(log_everywhere)
```

</details>

<details>
  <summary><b>Usage Statistics</b></summary>

- [PePy](https://pepy.tech/project/log-everywhere)
- [PyPi Stats](https://pypistats.org/packages/log-everywhere)
</details>
<p>
  <a href="https://pypistats.org/packages/log-everywhere"><img alt="PyPI - Daily Downloads" src="https://img.shields.io/pypi/dd/log-everywhere?labelColor=black&color=blue&label=PyPI%20downloads%20%28excludes%20mirrors%29" width="275"></a>
  <a href="https://pypistats.org/packages/log-everywhere"><img alt="PyPI - Weekly Downloads" src="https://img.shields.io/pypi/dw/log-everywhere?labelColor=black&color=yellow&label=PyPI%20downloads%20%28excludes%20mirrors%29"width="275"></a>
  <a href="https://pypistats.org/packages/log-everywhere"><img alt="PyPI - Monthly Downloads" src="https://img.shields.io/pypi/dm/log-everywhere?labelColor=black&color=blue&label=PyPI%20downloads%20%28excludes%20mirrors%29"width="275"></a>
  <br>
  <a href="https://pepy.tech/project/log-everywhere"><img alt="PePY Weekly Downloads" src="https://static.pepy.tech/personalized-badge/log-everywhere?period=week&units=international_system&left_color=black&right_color=yellow&left_text=PePY%20Downloads/week%20%28includes%20mirrors%29" width="275"></a>
  <a href="https://pepy.tech/project/log-everywhere"><img alt="PePY Monthly Downloads" src="https://static.pepy.tech/personalized-badge/log-everywhere?period=month&units=international_system&left_color=black&right_color=blue&left_text=PePY%20Downloads/month%20%28includes%20mirrors%29" width="275"></a>
  <a href="https://pepy.tech/project/log-everywhere"><img alt="PePY Total Downloads" src="https://static.pepy.tech/personalized-badge/log-everywhere?period=total&units=international_system&left_color=black&right_color=yellow&left_text=PePY%20Downloads%20Total%20%28includes%20mirrors%29" width="275"></a>
</p>

If you found this interesting or useful, **please consider starring this repo** on [GitHub](https://github.com/Shail-Shouryya/log-everywhere) so other people can more easily find and use this. Thanks!
