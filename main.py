from obswebsocket import obsws
from obswebsocket import requests as obs_requests
from time import sleep
import serial
import requests

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

if ser.isOpen():
    print("{} connected!".format(ser.port))

host = "localhost"
port = 4455
password = "secret"

CAMERA_IP = 'http://192.168.0.47'

ws = obsws(host, port, password)
ws.connect()


# Function to move the camera to a preset position
def move_camera_to_preset(preset_name):
    url = f'{CAMERA_IP}/axis-cgi/com/ptz.cgi'
    params = {
        'gotoserverpresetname': preset_name
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print(f'Successfully moved camera to preset: {preset_name}')
    else:
        print(f'Failed to move camera to preset: {response.status_code}, {response.text}')
    return response


def streamStatus():
    response = ws.call(obs_requests.GetStreamStatus())
    output_active = response.getOutputActive()
    print(output_active)
    return output_active

sleep(1)
streamActive = streamStatus()
msg = str(streamActive)
#byte_to_send = b'\x01' if streamActive else b'\x00'
print(msg)
ser.write(msg.encode())
sleep(1)
#set camera to starting location so UI led is accurate
move_camera_to_preset('Blake')
        
msg = 'Blake'
print(msg)
ser.write(msg.encode())
sleep(1)

line = 'void'
while True:
    
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
    
    if line == '1':
        streamActive = streamStatus()
        if(streamActive):
            ws.call(obs_requests.StopStream())
            sleep(.1)
        else:
            ws.call(obs_requests.StartStream())
            sleep(.1)
            
            
    if line == '2':
        move_camera_to_preset('Blake')
        """
        msg = 'Blake'
        print(msg)
        ser.write(msg.encode())
        """
        sleep(.1)
        
    if line == '3':
        move_camera_to_preset('Bench')
        """
        msg = 'Bench'
        print(msg)
        ser.write(msg.encode())
        """
        sleep(.1)
        
    line = 'void'


#ws.disconnect()