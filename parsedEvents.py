import requests
from requests.auth import HTTPDigestAuth
import xml.etree.ElementTree as ET

# Replace with your camera's IP and credentials
camera_ip = ""
username = "admin"
password = "your_password_here"

url = f"http://{camera_ip}/ISAPI/Event/notification/alertStream"
auth = HTTPDigestAuth(username, password)

WATCHED_EVENTS = ["motiondetection", "tamperdetection", "diskerror"]

def parse_event(xml_data):
    try:
        root = ET.fromstring(xml_data)
        event_type = root.findtext('.//{http://www.hikvision.com/ver20/XMLSchema}eventType')
        event_state = root.findtext('.//{http://www.hikvision.com/ver20/XMLSchema}eventState')
        timestamp = root.findtext('.//{http://www.hikvision.com/ver20/XMLSchema}dateTime')
        description = root.findtext('.//{http://www.hikvision.com/ver20/XMLSchema}eventDescription')
        channel = root.findtext('.//{http://www.hikvision.com/ver20/XMLSchema}channelName')

        return {
            "type": event_type,
            "state": event_state,
            "time": timestamp,
            "description": description,
            "channel": channel
        }

    except ET.ParseError:
        return None

def main():
    print("Listening for important events...\n")
    with requests.get(url, auth=auth, stream=True, timeout=30) as response:
        buffer = ""
         for line in response.iter_lines():
            if line:
                decoded_line = line.decode("utf-8")
                if decoded_line.startswith("<EventNotificationAlert"):
                    buffer = decoded_line
                elif "</EventNotificationAlert>" in decoded_line:
                    buffer += decoded_line
                    event_data = parse_event(buffer)
                    buffer = ""

                    if event_data and event_data["type"] in WATCHED_EVENTS:
                        print(f"\nALERT: {event_data['type'].upper()} detected!")
                        print(f"Time: {event_data['time']}")
                        print(f"Channel: {event_data['channel']}")
                        print(f"Description: {event_data['description']}")
                        print(f"State: {event_data['state']}\n")
            else:
                continue

if __name__ == "__main__":
    main()

