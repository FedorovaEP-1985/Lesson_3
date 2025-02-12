class Mailing:
    def __init__(self, to_adress, from_adress, weight, tracking_id):
        self.to_adress = to_adress
        self.from_adress = from_adress
        self.weight = weight
        self.tracking_id = tracking_id

    def __repr__(self) -> str:
        return f'Отправление: вес {self.weight}, трекинг-код {self.tracking_id}\nОткуда: {self.from_adress}\nКуда: {self.to_adress}'

   # def __str__(self):
    #return (f" отправление {self.trak} из {self.from_adress}"
                #f"в {self.to_adress} . Стоимость {self.cost} рублей.")