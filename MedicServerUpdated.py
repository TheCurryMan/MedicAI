from flask import Flask, request
import twilio.twiml
from twilio.rest import TwilioRestClient

app = Flask(__name__)
# Try adding your own number to this list!
account_sid = "ACa9eca256e7d2b82539a0c6086dc244d7"
auth_token = "213a8dd83633246a86c5b36361665220"
client = TwilioRestClient(account_sid, auth_token)


callers = {
    "+14252298079": "Avinash Jain",
}

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond and greet the caller by name."""
    body = request.values.get('Body', None)
    media = request.values.get('MediaUrl0', None)
    from_number = request.values.get('From', None)
    if from_number in callers:
        message = callers[from_number] + ", thanks for the message! " + body

    else:
        message = "Monkey, thanks for the message!"

    resp = twilio.twiml.Response()
    resp.message(message)
    resp.media(media)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)