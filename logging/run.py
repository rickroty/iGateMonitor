#docker run -p 24224:24224 -v /home/pi/projects/igatemonitor:/host -it logging:latest

hostip=""
from subprocess import check_output
ips=check_output(['hostname', '-I']).split()
for ip in ips:
        if ip[:3]=="192":
                hostip = ip
if hostip == "":
  print "Could not determine the host IP!"
  quit

envvar="HOSTIP=" + hostip
import docker
client = docker.from_env()

client.containers.run("logging:latest", detach=True, environment=envvar)
