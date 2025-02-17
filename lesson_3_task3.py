from address import Address
from mailing import Mailing


to_address = Address("Можайск", "Ватутина", "13", "24")
from_address = Address("Санкт-Петербург", "Невский", "5", "20")



my_mailing = Mailing(to_address, from_address, "F0222225", "500")
#print(my_mailing)

print(f"отправление {my_mailing.tracking_id} из {my_mailing.from_address.city}, {my_mailing.from_address.street}, {my_mailing.from_address.house_number} - {my_mailing.from_address.apartment_number}"
      f" в {my_mailing.to_address.city}, {my_mailing.to_address.street}, {my_mailing.to_address.house_number} - {my_mailing.to_address.apartment_number}. Стоимость {my_mailing.cost} рублей.")