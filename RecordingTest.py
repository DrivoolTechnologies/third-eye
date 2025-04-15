import requests
from requests.auth import HTTPDigestAuth

camera_ip = '192.xxx.x.xxx'  
username = 'admin'
password = ''

recording_endpoint = f'http://{camera_ip}/ISAPI/ContentMgmt/record'
response = requests.get(recording_endpoint, auth=HTTPDigestAuth(username, password))
print(response.text)

