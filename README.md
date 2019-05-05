[![LICENSE](https://img.shields.io/badge/license-Anti%20996-blue.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)
# CF-Cannon
## CF-Cannon is a tool written in python to perform layer 7 stress test on your own server.
# ---------------------------------------------
# V2 Version
## V2 version enables distributed attack on each nodes with penetration of Json protection page and can be (theoretically) deployed on infinite machines.
### Install:
```
apt-get update
apt-get -y upgrade
apt-get install build-essential nodejs python-setuptools
apt-get install -y python-pip
pip install demjson Flask pycurl 
```

### Run (on each node):
```
python attack.py
```
Then use any third party API Tester:(i.e https://apitester.com/)
```
attackinfo={
	"T": 8,
	"charset": "utf-8",
	"is_protected_by_cf": false,
	"keywords": "welcome",
	"path": "/index.php",
	"peerCount": 300,
	"threadCount": 10000000,
	"url": "http://www.sample.com"
}
```
##  Set "is_protected_by_cf" to be true only if you see following page:
![alt text](https://www.a2hosting.com/images/uploads/knowledgebase_images/kb-cloudflare-under-attack-interstitial-page.png)
# ---------------------------------------------

# V1 Version(NO LONGER UPDATED)

For CF-bypass you'll need a proxy list with very good connection and low latency to your server.

*Third party proxy checker you may need:*
https://github.com/maxmalysh/python-proxy-checker

### Install:
```
apt-get update
apt-get -y upgrade
apt-get install build-essential nodejs python-setuptools python3-setuptools
apt-get install -y python3-pip
pip3 install PySocks requests cfscrape scapy-python3
```

### Run:
```
python3 cf_cannon.py www.sample-target.com -t 1000 -d /index.php
```

### Parameters:
```
-d --dir : path of target, I.e: www.abc.com/index.php then -d /index.php
-s --ssl : Use http or https. For https&proxy mode your proxy must support https.
-p --port: Port of the server,80 or 443?
-t --threads: How many threads?
-l --time: Haven't done yet
-x --proxy_file_location : Deafult: proxy.list, feel free to assign other list.
```
### Don't forget:
```
ulimit -n 655350
```
### Proof of Power
![image](https://levyhsu.com/wp-content/uploads/2018/10/webwxgetmsgimg.jpeg)

### Notice that:
Each "ERROR:root:’http://abc.com’ returned an error. Could not collect tokens." indicates one proxy failure (cfscrape can’t access page though server)

The effiecy through proxy is still low, if you have ieda or update, welcome to merge.
