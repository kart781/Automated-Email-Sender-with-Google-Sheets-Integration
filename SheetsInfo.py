import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SPREADSHEET_ID = "Your Google Sheets ID"

credentials = None
if os.path.exists("token.json"):
    credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
if not credentials or not credentials.valid:
    if credentials and credentials.expired and credentials.refresh_token:
        credentials.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES) #Get your credentials from the Google Developer Console in the form of a JSON File
        credentials = flow.run_local_server(port=0)
    with open("token.json", "w") as token:
        token.write(credentials.to_json())

try:
    service = build("sheets", "v4", credentials=credentials)
    sheets = service.spreadsheets()

    result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range="Sheet1!C:C").execute()

    values = result.get("values")
    values = [item for sublist in values for item in sublist]
    values = values[1:]
    print(values)

except HttpError as error:
    print(error)


