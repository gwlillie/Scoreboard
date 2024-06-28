import gpiod
from obswebsocket import obsws, requests
from time import sleep

host = "localhost"
port = 4455
password = "secret"

ws = obsws(host, port, password)
ws.connect()

LED_PIN = 17
BUTTON_PIN = 27
chip = gpiod.Chip('gpiochip4')
led_line = chip.get_line(LED_PIN)
button_line = chip.get_line(BUTTON_PIN)
led_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)
button_line.request(consumer="Button", type=gpiod.LINE_REQ_DIR_IN)


try:
   while True:
       button_state = button_line.get_value()
       if button_state == 1:
           sleep(3)
           ws.call(requests.StartStream())
           while True:
               led_line.set_value(1)
               
               button_state = button_line.get_value()
               if button_state == 1:
                   ws.call(requests.StopStream())
                   sleep(3)
                   break
               
       else:
           led_line.set_value(0)
finally:
   led_line.release()
button_line.release()