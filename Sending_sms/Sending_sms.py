import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = '************'
auth_token = '************'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='Hi this is a test message!!',
         from_='+*********',
         to='+**********'
     )

print(message.sid)