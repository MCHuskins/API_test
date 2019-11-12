from flask import Flask
from twilio.rest import Client
#client is the progarme that talk to the twillio api
client = Client(account_sid, auth_token)
#stating flask
app = Flask(__name__)

@app.route("/")
def hello():
    message = client.messages.create(
                                  body='Guess how I send this -Matthew Huskins',
                                  from_='+16502036811',
                                  media_url=['https://media.tenor.com/images/4653cab601012d45914782bc482a6390/tenor.gif'],
                                  to='+16506789378'
                              )

    print(message.sid)
    return("message sent")

if __name__ == "__main__":
    app.run()
