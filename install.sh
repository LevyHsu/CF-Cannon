#!/bin/bash
apt-get update
apt-get -y upgrade
apt-get install build-essential nodejs python-setuptools
apt-get install -y python-pip
pip install demjson Flask pycurl