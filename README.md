# Simple File Browser (SFB)

Python REST API provides a way to list contents of a portion of a filesystem

## Installation
Run `make install` at the project root location to install and start the API

By default, the server is programmed to accept requests on `localhost:5000` or `0.0.0.0:5000` 

## Usage
Example : See sample request in `examples/run.sh`

`$ ./run.sh`

```
{
    "status_code": 200,
    "status_msg": "SUCCESS! Showing contents for /tmp",
    "error_desc": "",
    "contents": [
        {
            "info": {
                "filename": "tmpa9my2p6n",
                "uri": "/tmpa9my2p6n",
                "size": 259465,
                "permissions": "-rw-------",
                "owner": "root"
            },
            "folder": false
        },
        {
            "info": {
                "filename": "wv",
                "uri": "/wv",
                "size": 128,
                "permissions": "drwxr-xr-x",
                "owner": "root"
            },
            "folder": true
        },
        {
            "info": {
                "filename": "foo",
                "uri": "/foo",
                "size": 0,
                "permissions": "-rw-r--r--",
                "owner": "root"
            },
            "folder": false
        },
        {
            "info": {
                "filename": "foo7",
                "uri": "/foo7",
                "size": 0,
                "permissions": "-rw-r--r--",
                "owner": "root"
            },
            "folder": false
        }
    ],
    "timestamp": 1628323736
}

``` 

### API Docs
See `docs/simplefilebrowser` for API documentation
