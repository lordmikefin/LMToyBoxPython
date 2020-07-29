# -*- coding: UTF-8 -*-
'''
Created on 23 Jul 2020

@author: Mikko Niemelä

:copyright: (c) 2020, Mikko Niemelä a.k.a. Lord Mike (lordmike@iki.fi)
:license: MIT License
'''

from xml.etree.ElementTree import Element, SubElement


def create_subelem(elem: Element, tag_name: str=None, text: str=None):
    if not text:
        return  # do not create empty element
    elem = SubElement(elem, tag_name)
    elem.text = text


def indent(elem: Element, level=0):
    ''' Indent the xml tree '''
    # TODO: this should be part of 'xml.etree.ElementTree'
    # TODO: Send request to ElementTree toolkit project. Python core project?

    # NOTE: code copied from stackoverflow
    # https://stackoverflow.com/questions/3095434/inserting-newlines-in-xml-file-generated-via-xml-etree-elementtree-in-python
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i
