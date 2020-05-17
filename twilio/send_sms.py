from twilio.rest import Client
from credenteial import account_sid, auth_token, my_cell, my_twilio

client = Client(account_sid, auth_token)

my_msg = "Suhayb Cabdulahi"
message = client.messages.create(to = my_cell, from_ = my_twilio, body = my_msg)
