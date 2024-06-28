#!/usr/bin/env python3

import sys
import time

import logging
logging.basicConfig(level=logging.DEBUG)

sys.path.append('../')
from obswebsocket import obsws, requests, events  # noqa: E402

host = "localhost"
port = 4455
password = "secret"

ws = obsws(host, port, password)
ws.connect()

try:
    ws.call(requests.StartStream())
    time.sleep(10)
    ws.call(requests.StopStream())
    #scenes = ws.call(requests.GetSceneList())
    #for s in scenes.getScenes():
     #   name = s['sceneName']
      #  print("Switching to {}".format(name))
      #  ws.call(requests.SetCurrentProgramScene(sceneName=name))
      #  time.sleep(2)

    #print("End of list")
    #ws.call(events.ExitStarted())

except KeyboardInterrupt:
    pass

ws.disconnect()
