import requests
from requests.auth import HTTPDigestAuth

#replace with actual credentials
camera_ip = '192.xxx.x.xxx'
username = 'admin'
password = ''  
endpoint = f'http://{camera_ip}/ISAPI/System/deviceInfo'

response = requests.get(endpoint, auth=HTTPDigestAuth(username, password))

if response.status_code == 200:
    print("Device Info Received:")
    print(response.text)
else:
    print(f"Failed to fetch device info. Status Code: {response.status_code}")
    print("Response:", response.text)
