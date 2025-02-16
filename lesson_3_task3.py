from Adress import Adress
from Mailing import Mailing


to_adress = Adress("143204", "Можайск", "Ватутина", "13", "24")
from_adress = Adress("143204", "Можайск", "Ватутина", "26", "1")



my_mailing = Mailing(to_adress, from_adress, "500 г", "F0222225")

print(my_mailing)