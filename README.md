# Simple File Browser (SFB)

Python REST API provides a way to list contents of a portion of a filesystem

## Installation
In order to install `sfb-api`, follow these steps: 
1. `cd <path-to-simplefilebrowser>`
1. `export MNT_LOC=<root-dir-to-mount-for-query>`  set environment variable to root directory intended to be browsed/queried

2. Run `make install` at the project root location to install and start the API

By default, the server is programmed to accept requests on `localhost:5000/sfb/api` or `0.0.0.0:5000/sfb/api` 

## Usage
As part of using the API, following query parameters are available :

-`root`: Full path to root location of file/dir desired to be browsed

-`relpath` : Relative path to file/subdirectory as desired.


#### *Examples*
 
 - See sample request in `examples/run.sh` (shows contents of a folder for a sample request)
 
 `0.0.0.0:5000/sfb/api?root=${ROOT_DIR}&relpath=${RELPATH}`

`$ ./run.sh`

```
{
    "status_code": 200,
    "status_msg": "SUCCESS! Showing contents for /tmp/wv",
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

- Use a similar example for a path to a file on the host in order to return its contents
`curl -o resp.json -u calvin:hobbes http://0.0.0.0:5000/sfb/api?root=/tmp&relpath=/wv/foo`

```buildoutcfg
{
    "status_code": 200,
    "status_msg": "SUCCESS! Showing contents for /tmp/wv/foo",
    "error_desc": "",
    "contents": "this is a test\n",
    "timestamp": 1628458401
}

```
### API Docs
See `docs/simplefilebrowser` for API documentation
