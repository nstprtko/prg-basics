class BankAccount:
    def __init__(self, number):
        self.number = number 
        self.balance = 0

    def show_balance(self):
        print(f'Account number : {self.number}')
        print(f'Your balance is {self.balance}')
    
    def deposit(self, amount):
        self.amount = amount
        self.balance += round(self.amount,1)
        

    def withdraw(self, amount):
        self.amount = amount
        if self.balance < self.amount:
            print('Insufficient funds on the account')
        else:
            self.balance -= round(self.amount,1)
            print(f"You've withdrawed {self.amount}. Your balance is {round(self.balance,1)} ")

    
        