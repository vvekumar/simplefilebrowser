#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
import stat
import pathlib
from pwd import getpwuid
import logging
from simplefilebrowser.exceptions import *

class AccessNotPermitted(Exception):
    pass

class SimpleFileBrowser:
    """
    Provides a library of methods for browsing and returning contents of the host filesystem
    """
    def __init__(self):
        self.logger = logging.getLogger('__name__')

    def _is_file(self, path):
        """
        check "inode" is of a file type
        :param path: Path to check if is file or a not
        :return: True if file
        """
        if os.path.isfile(path):
            return True
        else:
            return False

    @staticmethod
    def get_file_info(file):
        """
        get information related to a file
        :param file: input file
        :return: (dict)

        ```
        e.g.
        get_file_info(foo) :
             {
            'filename': foo,
            'uri': '/' + foo,
            'size': 67K,
            'permissions': r--r--r--,
            'owner': johndoe
            }
        ```
        """
        name = os.path.basename(file)
        filestat = os.stat(file)
        size = filestat.st_size
        _mode = filestat.st_mode
        perms = stat.filemode(_mode)
        owner = getpwuid(os.stat(file)
                         .st_uid).pw_name

        return {
            'filename': name,
            'uri': '/' + name,
            'size': size,
            'permissions': perms,
            'owner': owner
        }

    def show_dir(self, path):
        """
        list directory and show following info about its entities : {name, owner, size, (octal permissions), if folder}
        :param path: input path directory
        :return: (list) return a list of dict with info on files

        """
        content = []
        if not os.path.exists(path):
            self.logger.error('Invalid path : ' + path)
            raise FileNotFoundError
        else:
            self.logger.info('Getting contents for ' + path)
        for (root, dirnames, filenames) in os.walk(path):
            for filename in filenames:
                try:
                    file = os.path.join(root, filename)
                    file_info = SimpleFileBrowser.get_file_info(file)
                    content.append({'info': file_info,
                                    'folder': False})
                except FileNotFoundError:
                    self.logger.error('Could not find file info for file : ' + file)
                    raise

            for dirname in dirnames:
                try:
                    dir = os.path.join(root, dirname)
                    dir_info = SimpleFileBrowser.get_file_info(dir)
                    content.append({'info': dir_info,
                                    'folder': True})
                except FileNotFoundError:
                    self.logger.error('Could not find file info for dir : ' + dir)
                    raise
        return content

    def show_file(self, path):
        """
        show contents of a file
        :param path: input file path
        :return: (list) contents of input file
        """
        self.logger.info('Showing contents of file : ' + path)
        contents = []
        with open(path) as file_path:
            contents = file_path.read()
        return contents

    def _is_access_allowed(self, path):
        """
        Check if access to file/directory is permitted
        :param path:
        :return:
        """
        # TODO
        return True

    def explore_location(self, path):
        """
        given an input path, return either its contents as the case may be for either a file/directory.
        :param path: input path
        :return:(list) contents of file/directory
        """
        if not self._is_access_allowed(path):
            raise
        if self._is_file(path):
            return self.show_file(path)
        else:
            return self.show_dir(path)
