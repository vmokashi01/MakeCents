import requests
import json
import config

fromCurrency = 'USD'
toCurrency = 'CAD'
amountToConvert = 200032
time = '2017-03-05'


xe_url = 'https://xecdapi.xe.com/v1/account_info'
xe_url_change = 'https://xecdapi.xe.com/v1/convert_from.json/'
xe_url_historic = 'https://xecdapi.xe.com/v1/historic_rate.json/'

account_sid = config.ACCOUNT_SID
auth_token = config.AUTH_KEY

payloadCurrencyConversion = {
	'from': fromCurrency,
	'to' : toCurrency,
	'amount' : amountToConvert
}

payloadHistoricRate = {
	'from': fromCurrency,
	'to' : toCurrency,
	'amount' : amountToConvert,
	'date' : time
}


current_rate = requests.get(xe_url_change, auth=(account_sid, auth_token), params=payloadCurrencyConversion)

historic_rate = requests.get(xe_url_historic, auth=(account_sid, auth_token), params=payloadHistoricRate)

print(historic_rate.text)
print(current_rate.text)
