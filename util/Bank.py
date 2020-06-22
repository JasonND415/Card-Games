from datetime import date
class Bank(self):
    def __init__(self):
        self.money=0
        self.date=date.today()
    def add(self,money):
        self.money+=money
    def get_amount(self):
        return self.money
    def withdraw(self,amount):
        if (self.money>=amount):
            self.money=self.money-amount
            return amount
        else:
            return 0
        
