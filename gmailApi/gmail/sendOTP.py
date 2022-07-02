from __future__ import print_function

import base64
from email.message import EmailMessage
import os
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
import random
from google_auth_oauthlib.flow import InstalledAppFlow
#SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
SCOPES = ['https://www.googleapis.com/auth/gmail.send']


def generate_OTP(length):
    OTP = ""
    for i in range(1,length):    
        a = chr(random.randrange(33,126))
        OTP+=a
    originalOTP = OTP
    return OTP


def OTP_Message(UserName,OTP):
    Msg = "Hi,\nWelcome " + UserName + "\nYour OTP is : "
    #OTP = generate_OTP(10)
    OTP = str(OTP)
    Msg+=OTP
    return Msg




def sendotp(MailID,UserName):
    """Create and send an email message
    Print the returned  message id
    Returns: Message object, including message id

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'gmailApi\gmail\credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    try:
        service = build('gmail', 'v1', credentials=creds)
        message = EmailMessage()
        OTPus = generate_OTP(10)
        message.set_content(OTP_Message(UserName,OTPus))

        message['To'] = MailID
        message['From'] = 'gduser2@workspacesamples.dev'
        message['Subject'] = 'OTP for Authentication'

        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()) \
            .decode()

        create_message = {
            'raw': encoded_message
        }
        # pylint: disable=E1101
        send_message = (service.users().messages().send
                        (userId="me", body=create_message).execute())
        print(F'Message Id: {send_message["id"]}')
    except HttpError as error:
        print(F'An error occurred: {error}')
        send_message = None
    return OTPus

