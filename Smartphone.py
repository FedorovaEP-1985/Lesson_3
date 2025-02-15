class Smartphone:
    def __init__(self, brand, model, number):
        self.brand = brand
        self.model = model
        self.number = number

    def __repr__(self):
        return f'Smartphone({self.brand}, {self.model}, {self.number})'

#def calls(self, kuki):
	#print("Звонил", self.number, "время", kuki )

