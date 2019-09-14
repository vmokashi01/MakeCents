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
	'from' : 'CAD',
	'to' : 'USD',
	'start_date' : '2017-09 22',
	'end_date' : '2019-09 10'
}

convertFrom = xecd.convert_from(currencyFrom, currencyTo, amount)
historicRate = xecd.historic_rate("2016-12-25", "12:34", currencyFrom, currencyTo, 55)
statsVolatility = requests.get(xe_volatility, auth=(account_sid, auth_token), params=payloadVolatility)

info = xecd.account_info()

print(statsVolatility)