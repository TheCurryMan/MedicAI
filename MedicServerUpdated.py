from flask import Flask, request
import twilio.twiml
from twilio.rest import TwilioRestClient
from getMessage import getMessage
import json

app = Flask(__name__)
# Try adding your own number to this list!
account_sid = "ACa9eca256e7d2b82539a0c6086dc244d7"
auth_token = "213a8dd83633246a86c5b36361665220"
client = TwilioRestClient(account_sid, auth_token)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond and greet the caller by name."""
    body = request.values.get('Body', None)
    img_url = request.values.get('MediaUrl0', None)
    from_number = request.values.get('From', None)

    message = getMessage(from_number, body, img_url)

    resp = twilio.twiml.Response()
    resp.message(message)
    return str(resp)



if __name__ == "__main__":
    app.run(debug=True)