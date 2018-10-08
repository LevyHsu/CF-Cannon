#!/bin/bash
apt-get update
apt-get -y upgrade
apt-get install build-essential nodejs python-setuptools python3-setuptools
apt-get install -y python3-pip
pip3 install PySocks requests cfscrape bs4 scapy-python3