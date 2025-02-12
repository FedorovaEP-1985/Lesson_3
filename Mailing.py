class Mailing:
    def __init__(self, to_address, from_address, weight, tracking_id):
        self.to_address = to_address
        self.from_address = from_address
        self.weight = weight
        self.tracking_id = tracking_id

    def __repr__(self):
        return f'Отправление: вес {self.weight}, трекинг-код {self.tracking_id}\nОткуда: {self.from_address}\nКуда: {self.to_address}'

   # def __str__(self):
    #return (f" отправление {self.trak} из {self.from_adress}"
                #f"в {self.to_adress} . Стоимость {self.cost} рублей.")