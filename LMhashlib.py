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


def print_progress(calculated, file_len):
    # create console progress bar
    # https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
    # https://stackoverflow.com/questions/3160699/python-progress-bar/3162864
    return print('Progress ' + str(calculated) + ' / ' + str(file_len))


def md5sum(src: str, length: int=io.DEFAULT_BUFFER_SIZE, callback=None,
           show_progress: bool=False) -> str:
    '''
    Calculate md5 checksum.

    https://www.geeksforgeeks.org/md5-hash-python/
    https://stackoverflow.com/questions/3431825/generating-an-md5-checksum-of-a-file
      NOTE: "The underlying MD5 algorithm is no longer deemed secure"
      TODO: Use SHA-2 or SHA-3 instead. For serucity.

    https://stackoverflow.com/questions/1131220/get-md5-hash-of-big-files-in-python/40961519#40961519
    '''
    file_len = Path(src).stat().st_size
    pbar = None
    if show_progress:
        pbar = tqdm(total=file_len)
    calculated = 0
    md5 = hashlib.md5()
    with io.open(src, mode="rb") as fd:
        for chunk in iter(lambda: fd.read(length), b''):
            md5.update(chunk)
            if not callback is None:
                calculated += len(chunk)
                callback(calculated, file_len)
            elif pbar:
                pbar.update(len(chunk))

    if pbar:
        pbar.close()
    # return md5
    return md5.hexdigest()


def sha256(src: str, length: int=io.DEFAULT_BUFFER_SIZE, callback=None,
           show_progress: bool=False) -> str:
    '''
    Calculate sha256

    based on md5sum(...) -function
    https://docs.python.org/2/library/hashlib.html
    '''
    logger.debug('Calculate sha256 sum for file: ' + str(src))
    file_len = Path(src).stat().st_size
    pbar = None
    if show_progress:
        pbar = tqdm(total=file_len)
    calculated = 0
    md5 = hashlib.sha256()
    with io.open(src, mode="rb") as fd:
        for chunk in iter(lambda: fd.read(length), b''):
            md5.update(chunk)
            if not callback is None:
                calculated += len(chunk)
                callback(calculated, file_len)
            elif pbar:
                pbar.update(len(chunk))

    if pbar:
        pbar.close()

    return md5.hexdigest()
