from Smartphone import Smart

catalog = []
catalog.append(Smart("Nokia", "2210", "+79152268093"))
catalog.append(Smart("Fly", "1111", "+79222222222"))
catalog.append(Smart("Motorola", "A4", "+79111111111"))
catalog.append(Smart("Samsung", "Galaxy11", "+7-999-123-45-67"))
catalog.append(Smart("IPhone", "13 ProMax", "+7-999-698-85-96"))

#phone.calls ("12:00")

for smart in catalog:
    #print(f"{smart.owner}, {smart.brand}, {smart.model}: {smart.number}")
    print(f" {smart.brand}, {smart.model}: {smart.number}")




