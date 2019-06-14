from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hello from Python Twilio Test!",
                     from_='+1 458 207 2741',
                     to='+84 36 7111 375'
                 )

print(message.sid)
