cd /host/monitoring
sbin/iwconfig > iwconfig.txt
python iwconfigparser.py iwconfig.txt
