from twilio.rest import Client
from config import account_sid,  auth_token

client = Client(account_sid, auth_token)

client.messages.create(
    to="...",
    from_="...",
    body = "I am checking on you. Automation"
)