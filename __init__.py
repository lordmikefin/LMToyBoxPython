# -*- coding: UTF-8 -*-
"""
    LMToyBoxPython
    ~~~~~~~~~~~~~~

    Module for collection of Lord Mike's Python toys :)

    License of this script file:
       MIT License

    License is available online:
      https://github.com/lordmikefin/LMToyBoxPython/blob/master/LICENSE

    Latest version of this script file:
      https://github.com/lordmikefin/LMToyBoxPython/blob/master/__init__.py


    :copyright: (c) 2020, Mikko Niemelä a.k.a. Lord Mike (lordmike@iki.fi)
    :license: MIT License
"""

import logging

__license__ = "MIT License"
__version__ = "0.0.7"
__revision__ = "LMToyBoxPython (module)  v" + __version__ + " (2020-07-23)"


def create_logger():
    # https://www.toptal.com/python/in-depth-python-logging
    log = logging.getLogger('LMToyBoxPython')
    # Do not propagate the log up to parent
    log.propagate = False
    return log

logger = create_logger()

def logging_test():
    logger.debug('LMToyBoxPython module logging test.')


def write_lines_to_file(file: str, lines: list, mode='w'):
    """
    Available modes:
    'w' open for writing, truncating the file first
    'x' open for exclusive creation, failing if the file already exists
    'a' open for writing, appending to the end of the file if it exists

    Read mode:
    https://docs.python.org/3/library/functions.html#open
    """
    with open(file, mode) as f:
        f.writelines(lines)
