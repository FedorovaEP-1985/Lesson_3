class Mailing:
    def __init__(self, to_address, from_address, tracking_id, cost):
        self.to_address = to_address
        self.from_address = from_address
        self.tracking_id = tracking_id
        self.cost = cost



    def __repr__(self):
        return f'Отправление: трекинг-код {self.tracking_id}, стоимость {self.cost}\nОткуда: {self.from_address}\nКуда: {self.to_address}'

   # def __str__(self):
    #return (f" отправление {self.trak} из {self.from_address}"
                #f"в {self.to_address} . Стоимость {self.cost} рублей.")