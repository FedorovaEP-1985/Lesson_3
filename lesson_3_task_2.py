from smartphone import Smartphone
from callLogger import CallLogger

#catalog = []
#catalog.append(Smartphone("Nokia", "2210", "+79152268093"))
#catalog.append(Smartphone("Fly", "1111", "+79222222222"))
#catalog.append(Smartphone("Motorola", "A4", "+79111111111"))
#catalog.append(Smartphone("Samsung", "Galaxy11", "+7-999-123-45-67"))
#catalog.append(Smartphone("IPhone", "13 ProMax", "+7-999-698-85-96"))

catalog = [ Smartphone("Nokia", "2210", "+79152268093"),
            Smartphone("Fly", "1111", "+79222222222"),
            Smartphone("Motorola", "A4", "+79111111111"),
            Smartphone("Samsung", "Galaxy11", "+7-999-123-45-67"),
            Smartphone("IPhone", "13 ProMax", "+7-999-698-85-96")]


for phone in catalog:
   print(f" {phone.brand}, {phone.model}: {phone.number}")

