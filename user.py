class User:
    first_name = {"Alena"}
    last_name = {"Fedorova"}
    my_name = "Вас зовут: {} {}".format(last_name, first_name)
    print (my_name)

    def __init__(self, name):
        self.name = name

    def first_name(self):
        print ("меня зовут", self.name)

    def last_name(self):
        print ("моя фамилия","Fedorova")


    #def abonent (self):
        #print ( "абонент по Имени", self.abonent)