import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying the sheet, use these scopes
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Path to your downloaded credentials.json file
CREDENTIALS_FILE = r'C:\Users\sayed\Desktop\Python Assignment\client_secret_509885066921-8lntqqq3o8buf8ibi3kl1kag1et940l4.apps.googleusercontent.com.json'

# Authenticate the user
def authenticate():
    creds = None
    # Check if token.pickle exists, it stores the user's credentials.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    # If there's no valid credentials available, let the user log in.
    if not creds or not creds.valid:
        print("No valid credentials found. Proceeding with login...")
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    # Build the API client
    service = build('sheets', 'v4', credentials=creds)
    print("Authentication successful!")
    return service

# Example function to read data from Google Sheets
def read_sheet(service, sheet_id):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=sheet_id, range="Sheet1!A1:D10").execute()
    values = result.get('values', [])
    return values

# Main execution
if __name__ == '__main__':
    print("Starting authentication...")
    service = authenticate()
    print("Authentication complete!")
    
    # Example sheet ID (replace with your actual Google Sheets ID)
    spreadsheet_id = 'your_google_sheet_id_here'
    
    # Call the read function (if you have a valid sheet ID)
    data = read_sheet(service, spreadsheet_id)
    print("Sheet data:")
    print(data)
