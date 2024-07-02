#import gpiod
from obswebsocket import obsws, requests
from time import sleep
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

host = "localhost"
port = 4455
password = "secret"

ws = obsws(host, port, password)
ws.connect()

#LED_PIN = 17
#BUTTON_PIN = 27
#chip = gpiod.Chip('gpiochip4')
#led_line = chip.get_line(LED_PIN)
#button_line = chip.get_line(BUTTON_PIN)
#led_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)
#button_line.request(consumer="Button", type=gpiod.LINE_REQ_DIR_IN)
line = 0


try:
   while True:
       #button_state = button_line.get_value()
       if ser.in_waiting > 0:
           line = ser.readline().decode('utf-8').rstrip()
           #print(line)
           if int(line):
               sleep(3)
               ws.call(requests.StartStream())
           #while True:
               #led_line.set_value(1)
               #if ser.in_waiting > 0:
                   #line = ser.readline().decode('utf-8').rstrip()
               #button_state = button_line.get_value()
               #if !line:
                #   ws.call(requests.StopStream())
                #   sleep(3)
                 #  line =="void"
                 #  break
               
           else:
               ws.call(requests.StopStream())
               sleep(3)
finally:
    print("Success")
   #led_line.release()
#button_line.release()