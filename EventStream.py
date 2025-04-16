import requests
from requests.auth import HTTPDigestAuth

camera_ip = 'xxx.xxx.x.xxx'
username = 'admin'
password = ''
endpoint = f'http://{camera_ip}/ISAPI/Event/notification/alertStream'

with requests.get(endpoint, auth=HTTPDigestAuth(username, password), stream=True) as response:
    if response.status_code == 200:
        print("Listening to event stream...")
        for line in response.iter_lines():
            if line:
                print(line.decode('utf-8'))
    else:
        print(f"Failed to connect to alert stream: {response.status_code}")
