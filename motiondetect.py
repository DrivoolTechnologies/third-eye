import requests
from requests.auth import HTTPDigestAuth

camera_ip = '192.xxx.xxx' 
username = 'admin'
password = ''

endpoint = f'http://{camera_ip}/ISAPI/System/Video/inputs/channels/1/motionDetection'

response = requests.get(endpoint, auth=HTTPDigestAuth(username, password))

if response.status_code == 200:
    print("Motion Detection Info Received:")
    print(response.text)
else:
    print(f"Failed to fetch motion detection info. Status Code: {response.status_code}")
    print("Response:", response.text)
