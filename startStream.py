from obswebsocket import obsws, requests

host = "localhost"
port = 4455
password = "secret"

ws = obsws(host, port, password)
ws.connect()

ws.call(requests.StartStream())


