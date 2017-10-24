#!/bin/bash
cd /home/ubuntu/
rm iwconfig.txt && sbin/iwconfig > iwconfig.txt
python iwconfigparser.py iwconfig.txt
