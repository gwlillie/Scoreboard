from gpiozero import LED
from time import sleep

led = LED(4)
x=1

try:
    while x<=3:
        led.on()
        print('...LED ON')
    
        sleep(1)
    
        led.off()
        print('LED OFF...')
    
        sleep(1)
        x+=1
    
except KeyboardInterrupt:
    
    pass