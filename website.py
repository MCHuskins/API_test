#TODO: label the "message input" box.
#TODO: create a new input field for the target phone number, and label that box too.
#TODO: (Optional) add a cool image/gif to the page



from flask import Flask, request, render_template
from twilio.rest import Client
import os
# Your Account SID from twilio.com/console
account_sid = os.environ["TWILLIO_ACCOUNT_SID"]
# Your Auth Token from twilio.com/console
auth_token  = os.environ["TWILLIO_AUTH_TOKEN"]

#client is the progarme that talk to the twillio api
client = Client(account_sid, auth_token)
#stating flask
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

#@app.route('/', methods=['POST'])
#def my_form_post():
    text = request.form['text']
    resever = request.form['resever']
    message = client.messages.create(
                                  body= text,
                                  from_='+17652272641',
                                  media_url=['https://media.tenor.com/images/4653cab601012d45914782bc482a6390/tenor.gif'],
                                  to= resever
                              )

    print(message.sid)
    return "message sent"

if __name__ == "__main__":
    app.run()
