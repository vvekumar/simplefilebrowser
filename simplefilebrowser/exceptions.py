#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Created by Vivek (Siri) Kumar on 7/31/21
"""
class Error(Exception):
    def __init__(self,):
        """Constructor for Error"""

class PathIsNotFile(Exception):
    pass

class AuthenticationException(Exception):
    pass
