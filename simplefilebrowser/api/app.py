#!/usr/bin/env python

import os
from flask import Flask, make_response
from flask_restful import Resource, Api
from simplefilebrowser.browser.filebrowser import SimpleFileBrowser, AccessNotPermitted
from flask import request
import time

app = Flask(__name__)
api = Api(app)


class SimpleFileBrowserAPI(Resource):
    def get_path(self):
        # construct lookup path from query string params
        args = request.args
        root = args.get('root')
        if args.get('relpath'):
            relpath = args.get('relpath').lstrip('/')
            fpath = os.path.join(root, relpath)
        else:
            fpath = root
        return fpath

    def authenticate(self):
        if request.authorization and request.authorization.username == 'calvin' \
                and request.authorization.password == 'hobbes':
                print("Authorized User")
                return True
        return False

    def get(self):
        if not self.authenticate():
            return make_response("Invalid username and/or password. Please verify.", 401, )
        error_desc = ""
        stimestamp = time.time()

        fpath = self.get_path()

        try:
            browser = SimpleFileBrowser()
            contents = browser.explore_location(fpath)
            status_code = 200
            status_msg = f"SUCCESS! Showing contents for {fpath}"
        except FileNotFoundError:
            contents = ""
            status_code = 400
            status_msg = "File not found"
            error_desc = "An invalid file/directory location was sent, please try a different location"
            pass
        except AccessNotPermitted:
            contents = ""
            status_code = 401
            status_msg = "Access not permitted"
            error_desc = "Access not permitted to file/directory. Please verify access and try again"
            pass

        response = {
            'status_code': status_code,
            'status_msg': status_msg,
            'error_desc': error_desc,
            'contents': contents,
            'stimestamp': int(stimestamp),
            'etimestamp': int(time.time())
        }
        return response

api.add_resource(SimpleFileBrowserAPI, '/sfb/api')

if __name__ == '__main__':
    # app.run(debug=True)  # USE FOR DEBUGGING ONLY!
    app.run()
