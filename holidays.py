from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import json

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

CURR_DIR = os.path.dirname(os.path.abspath(__file__)) + os.path.sep
TOKEN_FILE = CURR_DIR + "token.json"
CREDS_FILE = CURR_DIR + "credentials.json"
JSON_OUT_FILE = CURR_DIR + "holidays.json"


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())

    service = build("calendar", "v3", credentials=creds)

    # Get Panama Holidays
    now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time

    YEAR = datetime.datetime.now().year
    startDate = datetime.datetime(YEAR, 1, 1).isoformat() + "Z"
    endDate = datetime.datetime(YEAR, 12, 31).isoformat() + "Z"

    eventsResult = (
        service.events()
        .list(
            calendarId="es.pa#holiday@group.v.calendar.google.com",
            timeMin=startDate,
            timeMax=endDate,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )

    # Save Holidays to JSON file
    data = json.dumps(eventsResult)
    with open(JSON_OUT_FILE, "w", encoding="utf8") as json_file:
        json_file.write(data)


if __name__ == "__main__":
    main()
