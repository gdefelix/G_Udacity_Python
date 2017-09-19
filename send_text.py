from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC3aa026ef118732fe48f17db5a050c6ff"
# Your Auth Token from twilio.com/console
auth_token  = "a4db656f6d034833ffcaf21a972dae6e"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16506053060", 
    from_="+14159094335",
    body="My name is Ron Burgnady")

print (message.sid)
