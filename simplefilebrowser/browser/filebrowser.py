#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Created by Vivek Kumar on 7/27/21
"""

import os
import stat
import pathlib
from pwd import getpwuid
import logging
from simplefilebrowser.exceptions import *

class SimpleFileBrowser:
    def __init__(self):
        self.logger = logging.getLogger('__name__')

    def _valid_path(self, root):
        # TODO: may not be necessary
        if os.path.exists(root):
            return True
        else:
            return False

    def _is_file(self, path):
        if os.path.isfile(path):
            return True
        else:
            return False

    @staticmethod
    def get_file_info(file):
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
        # TODO: check permissions
        """
        List directory and show following info about its entities : {name, owner, size, (octal permissions), if folder}
        :param path:
        :return:
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
        # TODO: check permissions
        self.logger.info('Showing contents of file : ' + path)
        contents = []
        with open(path) as file_path:
            contents = file_path.read()
        return contents

    def explore_location(self, path):
        if self._is_file(path):
            return self.show_file(path)
        else:
            return self.show_dir(path)
