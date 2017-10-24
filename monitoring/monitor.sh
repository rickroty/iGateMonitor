#!/bin/sh
cd /home/ubuntu/
sbin/iwconfig > iwconfig.txt
python iwconfigparser.py iwconfig.txt
