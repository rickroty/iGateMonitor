from subprocess import check_output
ips=check_output(['hostname', '-I']).split()
for ip in ips:
        if ip[:3]=="192":
                print ip
