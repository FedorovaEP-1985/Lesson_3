class User:
    #first_name = {"Elena"}
    #last_name = {"Fedorova"}
    #my_name = "Вас зовут: {} {}".format(last_name, first_name)
    #print (my_name)


    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    def print_first_name(self):
        print (self.first_name)

    def print_last_name(self):
        print(self.last_name)

    def print_full_name(self):
        print(f"{self.first_name} {self.last_name}")

