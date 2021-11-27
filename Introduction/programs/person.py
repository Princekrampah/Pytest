class Person:
    def __init__(self, initial_amount = 0):
        self.amount = initial_amount
        self.saving = 0


    def recieve_income(self, income_amount):
        self.amount = self.amount + income_amount

    
    def create_expense(self, expense_amount):
        if self.amount < expense_amount:
            raise Exception("Insufficient fund")
        self.amount = self.amount - expense_amount


    def save(self):
        amount_to_save = (self.amount * 0.1)
        self.saving = self.saving + amount_to_save
        self.amount = self.amount - amount_to_save


          