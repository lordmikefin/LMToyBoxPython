# -*- coding: UTF-8 -*-
'''
Created on 23 Jul 2020

@author: Mikko Niemelä

:copyright: (c) 2020, Mikko Niemelä a.k.a. Lord Mike (lordmike@iki.fi)
:license: MIT License
'''

import io
import hashlib
from tqdm import tqdm
from pathlib import Path
from . import logger
from builtins import Exception


def print_progress(calculated, file_len):
    # create console progress bar
    # https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
    # https://stackoverflow.com/questions/3160699/python-progress-bar/3162864
    return print('Progress ' + str(calculated) + ' / ' + str(file_len))


def md5sum(src: str, length: int=io.DEFAULT_BUFFER_SIZE, callback=None,
           show_progress: bool=False) -> str:
    ''' Calculate md5 checksum.
      NOTE: Use SHA-2 or SHA-3 instead. For serucity.
    '''
    logger.debug('Calculate md5 sum for file: ' + str(src))
    return _hash_core(src, length, callback, show_progress, hashlib.md5())


def sha256(src: str, length: int=io.DEFAULT_BUFFER_SIZE, callback=None,
           show_progress: bool=False) -> str:
    ''' Calculate sha256 '''
    logger.debug('Calculate sha256 sum for file: ' + str(src))
    return _hash_core(src, length, callback, show_progress, hashlib.sha256())


def _hash_core(src: str, length: int=io.DEFAULT_BUFFER_SIZE, callback=None,
           show_progress: bool=False, hasher=None) -> str:
    '''
    Core function to calculate the has.

    https://docs.python.org/3/library/hashlib.html

    https://www.geeksforgeeks.org/md5-hash-python/
    https://stackoverflow.com/questions/3431825/generating-an-md5-checksum-of-a-file
      NOTE: "The underlying MD5 algorithm is no longer deemed secure"

    https://stackoverflow.com/questions/1131220/get-md5-hash-of-big-files-in-python/40961519#40961519
    '''
    if hasher is None:
        raise Exception('"hasher" parameter must be defined')

    file = Path(src)
    if not file.is_file():
        return ''  # NOTE: Return empty string on error !!!

    file_len = file.stat().st_size
    pbar = None
    if show_progress:
        pbar = tqdm(total=file_len)
    calculated = 0
    with io.open(src, mode="rb") as fd:
        # TODO: optimize - remove 'if-else' from the loop 
        for chunk in iter(lambda: fd.read(length), b''):
            hasher.update(chunk)
            if not callback is None:
                calculated += len(chunk)
                callback(calculated, file_len)
            elif pbar:
                pbar.update(len(chunk))

    if pbar:
        pbar.close()

    return hasher.hexdigest()
