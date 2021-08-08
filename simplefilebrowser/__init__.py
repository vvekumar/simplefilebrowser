#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
### **Introduction**

SimpleFileBrowser (SFB) provides a REST API for browsing locations in a filesystem as desired (upon setting up the base server)

### **Example**
To query the contents of folder `/tmp/wv` _(assumed exists on the host filesystem)_ and save in a results `resp.json` file

```$ curl -o resp.json -u ${USERNAME}:${PASSWORD} 0.0.0.0:5000/sfb/api?root=/tmp&relpath=/wv```

```$ cat resp.json```

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

### **Error Codes**

`200` :: Success

`400` :: File not found

`401` :: Invalid username and/or password

### **Assumptions**
- Docker mounts desired directories during deployment (having the effect of only providing mounted directories available through the API for browsing)
- Support if there for mounting a single directory location for browsing (while it is entirely possible in order to provide
multiple directories to be mounted for browsing
"""