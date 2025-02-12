class Adress:
   def __init__(self, zip_code, city, street, house_number, apartment_number):
      self.zip_code = zip_code
      self.city = city
      self.street = street
      self.house_number = house_number
      self.apartment_number = apartment_number

   def __repr__(self):
      return f'Адрес: индекс {self.zip_code}, город {self.city}, улица {self.street}, дом {self.house_number}, квартира {self.apartment_number}'
   #def str (self):
       #eturn f"(self.index), (self.city), (self.street), (self-house) - (self-apartment)"