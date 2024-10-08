#!/usr/bin/env python3

import sys
import time

import logging
logging.basicConfig(level=logging.DEBUG)

sys.path.append('../')
from obswebsocket import obsws, events  # noqa: E402

host = "localhost"
port = 4455
password = "secret"


#def on_event(message):
 #   print("Got message: {}".format(message))


#def on_switch(message):
 #   print("You changed the scene to {}".format(message.getSceneName()))


ws = obsws(host, port, password)
#ws.register(on_event)
#ws.register(on_switch, events.SwitchScenes)
#ws.register(on_switch, events.CurrentProgramSceneChanged)
ws.connect()

try:
#     print("OK")
#     time.sleep(10)
#     print("END")
    ws.call(events.ExitStarted())
    time.sleep(10)

except KeyboardInterrupt:
    pass

ws.disconnect()