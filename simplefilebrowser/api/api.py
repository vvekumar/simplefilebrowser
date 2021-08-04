#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Created by Vivek Kumar on 7/27/21

"""
from flask import Flask
from flask_restful import Resource, Api
from simplefilebrowser.browser.filebrowser import SimpleFileBrowser
import requests
from flask import request
import time

app = Flask(__name__)
api = Api(app)


class SimpleFileBrowserAPI(Resource):
    def __init__(self,):
        pass

    @app.route('/data')
    def data(self):
        # here we want to get the value of user (i.e. ?user=some-value)
        fpath = request.args.get('param0')
        return fpath

    def test_code(self):
        # TODO : show sample contents
        # TEST CODE
        browser = SimpleFileBrowser()

        # dirpath = "/Users/vivekk_28/Vi/code/playground/github/simplefilebrowser/simplefilebrowser/api"
        filepath = "/Users/vivekk_28/Vi/code/playground/github/simplefilebrowser/simplefilebrowser/exceptions.py"
        # contents = browser.explore_location(dirpath)
        contents = browser.explore_location(filepath)
        return contents

    def get(self):
        # TODO:  Add BasicHTTPAuth (get user)
        # TODO: Accept JSON request param for location (  -d '{"param0":"/home/my_user/otherstuff/foo/​"}' \
        # Call test code
        error_desc = ""
        timestamp = time.time()
        try:
            contents = self.test_code()
            # fpath = self.data()
            # browser = SimpleFileBrowser()
            # contents = browser.explore_location(fpath)
            status_code = 200
            status_msg = "Success"
        except FileNotFoundError:
            contents = ""
            status_code = 400
            status_msg = "File not found"
            error_desc = "An invalid file/directory location was sent, please try a different location"
            pass
        except AuthenticationException:
            pass
        response = {
            'status_code': status_code,
            'status_msg': status_msg,
            'error_desc': error_desc,
            'contents': contents,
            'timestamp': int(timestamp)
        }
        return response


api.add_resource(SimpleFileBrowserAPI, '/')

if __name__ == '__main__':
    # app.run(debug=True) # USE FOR DEBUGGING ONLY!
    app.run()
