class Address:
   def __init__(self,  city, street, house_number, apartment_number):
      self.city = city
      self.street = street
      self.house_number = house_number
      self.apartment_number = apartment_number

   def __repr__(self):
      return f'Адрес: и город {self.city}, улица {self.street}, дом {self.house_number}, квартира {self.apartment_number}'
