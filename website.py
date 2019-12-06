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

#client is the program that talks to the twillio api
client = Client(account_sid, auth_token)
#starting flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def my_form():
    return render_template('my-form.html')

# @app.route('/', methods=['POST'])
# def my_form_post():
#     form_message = request.form['message']
#     form_number = request.form['form_number']
#     print(form_message)
#     print(form_number)
#     message = client.messages.create(
#                                   body= form_message,
#                                   from_='+17652272641',
#                                   media_url=['https://media.tenor.com/images/4653cab601012d45914782bc482a6390/tenor.gif'],
#                                   to= form_number
#                               )

#     print(message.sid)
#     return "message sent"

@app.route('/', methods=['POST'])
def my_form_post():
    form_message = request.form['msg']
    form_number = request.form['target_num']
    print(form_message)
    print(form_number)
    message = client.messages.create(
                                  body= form_message,
                                  from_='17652272641',
                                  media_url=['https://media.tenor.com/images/4653cab601012d45914782bc482a6390/tenor.gif'],
                                  to= form_number
                              )

    print(message.sid)
    return f"your message was was {request.form['msg']} and target number was {request.form['target_num']}"

if __name__ == "__main__":
    app.run()
