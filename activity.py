from stravalib.client import Client

import auth_data

client = Client()

access_token = auth_data.ACCESS_TOKEN
refresh_token = auth_data.REFRESH_TOKEN
expires_at = auth_data.EXPIRE_AT

# Now store that short-lived access token somewhere (a database?)
client.access_token = access_token
# You must also store the refresh token to be used later on to obtain another valid access token
# in case the current is already expired
client.refresh_token = refresh_token

# An access_token is only valid for 6 hours, store expires_at somewhere and
# check it before making an API call.
client.token_expires_at = expires_at

athlete = client.get_athlete()
print("Hello, mr {}".format(athlete.lastname))
print("Your profile:")
print(athlete)
