# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACc02a6cd029be8e49f8003dff669ba146'
auth_token = 'bdee4244d1652feedc48987d5bcc87c9'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Guess how I send this -Matthew Huskins',
                              from_='+16502036811',
                              media_url=['https://media.tenor.com/images/4653cab601012d45914782bc482a6390/tenor.gif'],
                              to='+16506789378'
                          )

print(message.sid)
