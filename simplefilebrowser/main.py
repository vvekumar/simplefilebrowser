#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Created by Vivek Kumar on 7/27/21
"""
import sys
import logging

def set_logger(log_file=None):
    """
    Set logger module
    """
    if log_file:
        logging.basicConfig(filename=log_file,
                            level=logging.INFO,
                            format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    else:
        logging.basicConfig(stream=sys.stdout,
                            level=logging.INFO,
                            format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')

if __name__ == '__main__':
    set_logger()
