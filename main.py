import requests

class main:
	def __init__(self):
		super().__init__()
		self.baseCur = input('Enter base currency symbolic notation: ')
		self.response = requests.get(f'https://v6.exchangerate-api.com/v6/c7aeeeb09a5d7c5ab1c47383/latest/{self.baseCur}')
		self.data = self.response.json()  # Getting data in json format
		self.conversion = self.data['conversion_rates']  # Getting values and symbolic notations of currencies

	def conversion_Base_to_Opted(self):
		self.usrINP = input(f'How many {self.baseCur}: ')
		self.usrOPT = input(f'Enter currency code to which {self.usrINP} {self.baseCur} will be converted: ')
		try:
			self.usrINP = float(self.usrINP)
			if self.usrOPT in self.conversion:
				self.usrOPT_VAL = self.conversion.get(self.usrOPT)
				print(f'{self.usrINP} INR --> {self.usrOPT_VAL * self.usrINP} {self.usrOPT}')
		except Exception as e:
			print(e)

if __name__ == '__main__':
	main = main()
	main.conversion_Base_to_Opted()