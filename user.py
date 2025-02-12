class User:
    first_name = {"Lena"}
    last_name = {"Fedorova"}
    my_name = "Вас зовут: {} {}".format(last_name, first_name)
    print (my_name)

    def __init__(self, name):
        print("я тут")
        self.username = name

    def first_name(self):
            print("меня зовут ", self.username)

    def last_name(self):
            print("моя фамилия ", "Fedorova")

    def SONAME(self, first_name, input):
            print("меня зовут ", self.username, input)
            self.last_name = input      

    def abonent (self):
        print ( "абонент по Имени", self.abonent)