from flask import Flask, request, render_template
import twilio.twiml
from twilio.rest import TwilioRestClient
from getMessage import getMessage
import json

"""
Overall flask app
"""

app = Flask(__name__)
# Try adding your own number to this list!
account_sid = "ACa9eca256e7d2b82539a0c6086dc244d7"
auth_token = "213a8dd83633246a86c5b36361665220"
client = TwilioRestClient(account_sid, auth_token)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():

    #Getting actual message from user
    body = request.values.get('Body', None)

    #Getting any image the user might have sent
    img_url = request.values.get('MediaUrl0', None)

    #Getting the from number from the user
    from_number = request.values.get('From', None)

    #Gets the message that's returned back to the user
    message = getMessage(from_number, body, img_url)

    #Sends the message back
    resp = twilio.twiml.Response()
    resp.message(message)
    return str(resp)

@app.route('/crawl')
def crawl():
    return render_template('crawl.html', myfunction=search)


if __name__ == "__main__":
    app.run(debug=True)