import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import re
from file_selector import link


SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

def get_column_data():

    
    pattern = r'd/([a-zA-Z0-9_-]+)/'
    match = re.search(pattern, link)

    SPREADSHEET_ID = None
    if match:
        SPREADSHEET_ID = match.group(1)

    # At this point, SPREADSHEET_ID will either contain the extracted ID or None
    if SPREADSHEET_ID:
        print("Document ID:", SPREADSHEET_ID)
    else:
        print("No valid document ID found in the URL.")
    
    credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(credentials.to_json())

    try:
        service = build("sheets", "v4", credentials=credentials)
        sheets = service.spreadsheets()

        result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range="Sheet1!C:C").execute()

        values = result.get("values")
        values = [item for sublist in values for item in sublist]
        
        # values = values[1:]
        return values
        
    except HttpError as error:
        print(error)