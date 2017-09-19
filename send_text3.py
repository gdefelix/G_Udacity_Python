from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC4e5ba919836f7760ec5122940f0e7082"
# Your Auth Token from twilio.com/console
auth_token  = "0850b36e3b31c0d2697f5a768db8219f"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16506053060", 
    from_="+14159094335",
    body="My name is Ron Burgnady")

print (message.sid)
