class Account:
    def __init__(self, name, number):
        self.name    = name
        self.number  = number
        self.balance = 0

    def deposit(self, money):
        if money <0:
            raise ValueError("money must be positive")
        self.balance+=money
        print('Your balance is {}'.format(self.balance))

    def withdraw(self, money):
        if money <0:
            raise ValueError("money must be positive")

        if money>self.balance:
            raise RuntimeError("sorry! your balance is not enough!")

        self.balance-=money
        print('Your balance is {}'.format(self.balance))

# ===

eric = Account(name='Eric', number=1234)
eric.deposit(money=100000)
eric.withdraw(money=50000)

        
