class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money

    def withdraw(self, money):
        if self.balance > money:
            self.balance -= money
        else:
            print('You don\'t have enough money')


class Owner(BankAccount):
    pass

    def __init__(self, owner, balance, credit_card_number, password):
        super().__init__(owner, balance)
        self.credit_card_number = credit_card_number
        self.password = password

    def check_owner_info(self, credit_card_number, password):
        for i in range(2):
            passwrd = input('Password')
            if self.password == passwrd:
                answer = input('do you want to deposit or withdraw')
                if answer == "deposit":
                    money = int(input("money: "))
                    self.deposit(money)
                elif answer == 'withdraw':
                    money = int(input('money:'))
                    self.withdraw(money)
                    return
            else:
                print("wrong password, you have one chance left")
        print('Your card has been eaten')


bk = BankAccount(owner="Omri", balance=20000000)

print(bk.balance)