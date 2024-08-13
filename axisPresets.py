import requests
from time import sleep

# Replace with your camera's IP address, username, and password if needed
CAMERA_IP = 'http://192.168.0.47'

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

# Example usage
move_camera_to_preset('Door')  # Replace 'Preset1' with the actual preset name
sleep(3)
move_camera_to_preset('Oven')  # Replace 'Preset2' with another preset name
sleep(3)
move_camera_to_preset('Hall')