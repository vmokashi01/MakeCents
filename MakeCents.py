import config
import requests
import json
from xecd_rates_client import XecdClient

account_sid = config.ACCOUNT_SID
auth_token = config.AUTH_KEY

xecd = XecdClient(account_sid, auth_token)

xe_volatility = 'https://xecdapi.xe.com/v1/stats'

currencyFrom = "CAD"
currencyTo = "USD"
amount = "2"

payloadVolatility = {
	'from' : 'USD',
	'to' : 'CAD',
	'start_date' : '2019-01-01'
}

statsVolatility = requests.get(xe_volatility, auth=(account_sid, auth_token), params=payloadVolatility)

print(statsVolatility.text)