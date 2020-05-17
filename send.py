

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC42d5f99b7dad1b369d116be1f9dea924"
# Your Auth Token from twilio.com/console
auth_token  = "ebc9ec75d4d799064f51fa9786f92252"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+252616989940", 
    from_="+33974591987",
    body="Hello from Python!")

print(message.sid)
