from __future__ import print_function
#from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file,client,tools
from googleapiclient import sample_tools
import datetime
import sys

def main(argv):

    f = open('event_list.txt','w')

    service, flags = sample_tools.init(
        argv, 'calendar', 'v3', __doc__, __file__,
        scope='https://www.googleapis.com/auth/calendar.readonly')

    try:
        page_token = None
        while True:

            calendar_list = service.calendarList().list(pageToken=page_token).execute()
            page_token = calendar_list.get('nextPageToken')

            now = datetime.datetime.utcnow().isoformat() + 'Z'
            events_result = service.events().list(calendarId='primary',timeMin=now,
                                                    maxResults=10,singleEvents=True,
                                                    orderBy='startTime').execute()
            events = events_result.get('items',[])
            for event in events:
                start = event['start'].get('dateTime',event['start'].get('date'))
                print(start,event['summary'],file=f)

            if not page_token:
                break

    except client.AccessTokenRefreshError:
        print('The credentials have been revoked or expired, please re-run'
            'the application to re-authorize.')

    f.close()

if __name__ == '__main__':
    main(sys.argv)
