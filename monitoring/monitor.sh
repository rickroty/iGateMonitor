cd /home/ubuntu/monitoring
sbin/iwconfig > iwconfig.txt
python iwconfigparser.py iwconfig.txt
