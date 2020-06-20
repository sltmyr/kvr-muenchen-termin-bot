import json
import re
import time
from datetime import datetime

import boto3
import requests

url = 'https://www22.muenchen.de/view-fs/termin/index.php'
body = {
    'CASETYPES[FS Umschreibung Ausländischer FS]': 1,
    'step': 'WEB_APPOINT_SEARCH_BY_CASETYPES',
}

appointment_type = 'Termin FS Allgemeinschalter_G'
sns_topic_arn = 'arn:aws:sns:eu-west-1:678739632517:kvr-termin'

while True:
    s = requests.Session()
    s.post(url)  # First request to get and save cookies
    response = s.post(url, body)

    try:
        json_str = re.search('jsonAppoints = \'(.*?)\'',
                             response.text).group(1)
    except AttributeError:
        print(
            f"ERROR: cannot find appointment data in server's response: {response}")

    appointment_data = json.loads(json_str)
    appointments = appointment_data[appointment_type]['appoints']

    available = False
    for day in appointments:
        if len(appointments[day]):
            message = f'appointment available on {day} at {appointments[day]}'
            print(message)
            available = True
            client = boto3.client('sns', region_name='eu-west-1')
            client.publish(
                TopicArn=sns_topic_arn,
                Message=message
            )
    if not available:
        print(
            f'{datetime.now().strftime("%H:%M:%S")}: no appointment available: {appointments}')
    time.sleep(60)
