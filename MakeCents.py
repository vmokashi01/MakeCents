import requests
import json
import config

fromCurrency = 'USD'
toCurrency = 'CAD'
amountToConvert = 200032

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
	'date' : amountToConvert,
	'time'
}


response = requests.get(xe_url_change, auth=(account_sid, auth_token), params=payloadCurrencyConversion)
print(response.text)