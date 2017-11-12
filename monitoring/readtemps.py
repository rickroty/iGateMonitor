import os
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

temp_sensor_inside = '/sys/bus/w1/devices/28-03146d1044ff/w1_slave'

temp_sensor_outside = '/sys/bus/w1/devices/28-0215155c4aff/w1_slave'

# read row data

def temp_raw(temp_sensor):
    f=open(temp_sensor,'r')
    lines=f.readlines()
    f.close()
    return lines

# parse row data
def read_temp(temp_sensor):
    lines=temp_raw(temp_sensor)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines=temp_raw(temp_sensor)

# get temperature output
# we can find it at this row 74 01 4b 46 7f ff 0c 10 55 t=23250
# t=23250

    temp_output = lines[1].find('t=')

    if temp_output != -1:
        temp_string = lines[1].strip()[temp_output+2:]
        temp_c = float(temp_string)/1000.0    # Celsius
        #temp_f = temp_c * 9.0 / 5.0 + 32.0    # Fahrenheit
        return temp_c
     else:
        return -1
       
inside_temp = read_temp(temp_sensor_inside)

outside_temp = read_temp(temp_sensor_outside)

timestamp = int(time.time())
hostname = os.environ['HOSTIP']
uri='http://' + hostname + ':24224/temperature'
data={"APRS_station": "KG7TMT-10", "inside_temp": inside_temp, "outside_temp": outside_temp, "date": timestamp}

print "Writing stats to: " + uri
			
print json.dumps(data, indent=4, sort_keys=True)

r = requests.post(uri, json=data)
print "response status=" + str(r.status_code)

