import requests
from requests.auth import HTTPDigestAuth

#Replace with actual credentials
camera_ip = '192.xxx.x.xxx'
username = 'admin'
password = ''

endpoint = f'http://{camera_ip}/ISAPI/System/Network/interfaces'

response = requests.get(endpoint, auth=HTTPDigestAuth(username, password))

if response.status_code == 200:
    print("Network Interface Info:")
    print(response.text)
else:
    print(f"Failed to fetch network info. Status Code: {response.status_code}")
    print("Response:", response.text)

endpoint = f'http://{camera_ip}/ISAPI/ContentMgmt/storage'

response = requests.get(endpoint, auth=HTTPDigestAuth(username, password))

if response.status_code == 200:
    print("Storage Info Received:")
    print(response.text)
else:
    print(f"Failed to fetch storage info. Status Code: {response.status_code}")
    print("Response:", response.text)

