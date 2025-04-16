import requests
from requests.auth import HTTPDigestAuth

camera_ip = '192.xxx.x.xxx'
username = 'admin'
password = ''
endpoint = f'http://{camera_ip}/ISAPI/Event/triggers'

response = requests.get(endpoint, auth=HTTPDigestAuth(username, password))

if response.status_code == 200:
    print("Event Triggers Info Received:")
    print(response.text)
else:
    print(f"Failed to fetch event triggers. Status Code: {response.status_code}")

