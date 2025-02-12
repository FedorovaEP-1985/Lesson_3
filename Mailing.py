class Mailing:

	def __init__(self, to_adress, from_adress, cost, trak):
		self.to_adress = to_adress
		self.from_adress = from_adress
		self.cost = cost
		self.trak = trak

     def __str__(self):
        return (f" отправление {self.trak} из {self.from_adress}"
                f"в {self.to_adress} . Стоимость {self.cost} рублей.")