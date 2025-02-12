class Smart:
	number = '+70000000000'
	model_phone = 'model'
	phone_brand = 'brand'
	abonent= "FIO"

	def __init__(self, brand, model, number, abonent):
		self.number = number
		self.model_phone = model
		self.phone_brand = brand 
		self.abonent = abonent

	def calls(self, kuki):
		print("Звонил", self.number, "время", kuki )