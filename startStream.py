from obswebsocket import obsws, requests

host = "localhost"
port = 4455
password = "secret"

ws = obsws(host, port, password)
ws.connect()

def streamStatus():
    response = ws.call(requests.GetStreamStatus())
    output_active = response.getOutputActive()
    print(output_active)
    return output_active
#response = 'void'
#response = ws.call(requests.GetStreamStatus())
#print(response)

# = 'void'
#status = response['outputActive']
#print(status)

ws.call(requests.StartStream())
streamStatus()

ws.disconnect()

