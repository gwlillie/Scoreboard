#!/usr/bin/env python3

import sys
import time
#time.sleep(60)
import logging
logging.basicConfig(level=logging.DEBUG)

sys.path.append('../')
from obswebsocket import obsws, requests  # noqa: E402
from pyautogui import press, typewrite, hotkey

host = "localhost"
port = 4455
password = "secret"

ws = obsws(host, port, password)
ws.connect()

try:
    ws.call(requests.StartStream())
    time.sleep(10)
    ws.call(requests.StopStream())
    time.sleep(25)
    hotkey('ctrl', 'q')
    #scenes = ws.call(requests.GetSceneList())
    #for s in scenes.getScenes():
     #   name = s['sceneName']
      #  print("Switching to {}".format(name))
      #  ws.call(requests.SetCurrentProgramScene(sceneName=name))
      #  time.sleep(2)

    #print("End of list")

except KeyboardInterrupt:
    pass

ws.disconnect()
print("disconnected")