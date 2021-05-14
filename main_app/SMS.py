import os
from twilio.rest import Client
from pathlib import Path
# Your Account Sid and Auth Token from twilio.com/console
# All the account credantials are saved in .env file
from dotenv import load_dotenv
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dotenv_path=env_path=Path(BASE_DIR)/'.env'

load_dotenv(dotenv_path=dotenv_path)




account_sid =  os.getenv('TWILIO_ACCOUNT_SID',None)
auth_token = os.getenv('TWILIO_AUTH_TOKEN',None)
RESCUE_TEAM_MOBILE = os.getenv('RESCUE_TEAM_MOBILE',None)





def send_sms(numbers,name,link): 
   message_body=f'''🚨🛑 *Emergency* 🛑🚨{name} is in emergency and need your help immediately.
                   Click the link below for location
                   {link}'''

   for x in range(len(numbers)):
      if account_sid is not None and auth_token is not None:
               client = Client(account_sid, auth_token)

               if RESCUE_TEAM_MOBILE is not None:
                 message= client.messages \
                        .create(
                          body=message_body,
                          from_=RESCUE_TEAM_MOBILE,
                          to=numbers[x]
                        )
      else:
         raise Exception('Account Credentials Not Found')          