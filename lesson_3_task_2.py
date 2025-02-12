from user import User
from Smartphone import Smart


Helen = User("Lena")
Helen.first_name()
Helen.abonent()


smartphone_1 = Smart (["Nokia"], ["2210"], ["+79152268093"], ["Danya"])
smartphone_2 = Smart (["Fly"], ["1111"], ["+79222222222"], ["Oly"])
smartphone_3 = Smart (["Motorola"], ["A4"], ["+79111111111"], ["Dima"])

#Smart_1.class_attribute = "Smartphone"
#print(smart_1.class_attribute)

smartphone_1.calls ("12:00")


print(smartphone_1)
print(smartphone_2)
print(smartphone_3)
print(smartphone_1)
print(smartphone_2)

