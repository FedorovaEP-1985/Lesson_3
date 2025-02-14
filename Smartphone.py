class Smart:
    def __init__(self, brand, model, number):
        self.number = number
        self.model = model
        self.brand = brand
        #self.owner = owner

    def __repr__(self):
        return f'Smart({self.brand}, {self.model}, {self.number})'

#def calls(self, kuki):
	#print("Звонил", self.number, "время", kuki )

