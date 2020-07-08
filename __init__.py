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
__version__ = "0.0.1"
__revision__ = "LMToyBoxPython (module)  v" + __version__ + " (2020-07-08)"

def create_logger():
    # https://www.toptal.com/python/in-depth-python-logging
    log = logging.getLogger('LMToyBoxPython')
    # Do not propagate the log up to parent
    log.propagate = False
    return log

logger = create_logger()

def logging_test():
    logger.debug('LMToyBoxPython module logging test.')
