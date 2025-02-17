class CallLogger:
    def __init__(self, number):
        self.number = number
        self.kuki = None

    def calls(self, kuki):
     print("Звонил", self.number, "время", kuki )
     self.kuki =kuki

