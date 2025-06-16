import gradio as gr
import pandas as pd
from datetime import datetime, timedelta
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import os

SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_calendar_service():
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    return build('calendar', 'v3', credentials=creds)

def create_event(service, row):
    client = row['Client']
    date_str = f"{row['Date']} {row['Time']}"
    start = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
    end = start + timedelta(minutes=int(row['Duration']))

    event = {
        'summary': f"Meeting with {client}",
        'description': row.get('Details', ''),
        'start': {'dateTime': start.isoformat(), 'timeZone': 'Asia/Kolkata'},
        'end': {'dateTime': end.isoformat(), 'timeZone': 'Asia/Kolkata'},
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 30},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }
    service.events().insert(calendarId='primary', body=event).execute()

def process_excel(file):
    df = pd.read_excel(file.name)
    service = get_calendar_service()
    for _, row in df.iterrows():
        create_event(service, row)
    return "✅ Calendar events created successfully!"

gr.Interface(
    fn=process_excel,
    inputs=gr.File(file_types=[".xlsx"]),
    outputs="text",
    title="Client Meeting Scheduler",
    description="Upload an Excel file to create Google Calendar events with Gmail reminders."
).launch()
