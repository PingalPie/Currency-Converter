import requests

# Getting currency data
response = requests.get('https://v6.exchangerate-api.com/v6/c7aeeeb09a5d7c5ab1c47383/latest/INR')
data = response.json() # Getting data in json format
conversion = data['conversion_rates'] # Getting values and symbolic notations of currencies
usrINR = input('How many INR: ')
usrOPT = input(f'Enter currency code to which {usrINR} INR will be converted: ')
try:
	usrINR = float(usrINR)
	if usrOPT in conversion:
		usrOPT_VAL = conversion.get(usrOPT)
		print(f'{usrINR} INR --> {usrOPT_VAL*usrINR} {usrOPT}')
except Exception as e:
	print(e)
