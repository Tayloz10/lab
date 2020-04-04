class Account:
    def __init__(self, name = None, number = 0, balance = 0):
        self.name = name
        self.number = number
        self.balance = balance
    def __srt__(self):
        return("Account Name: {}\n""Account Number: {}\n""Account Balance: ${}\n" .format(self.name, self.number, self.balance))
if __name__ == "__main__":
    account1 = Account("Trish Duce", 90453889, 100.00)
    account2 = Account("Donald Duck", 74773321, 100.00)
    account3 = Account("Joe Smith", 74773321, 150.00)
    print(account1)
    print(account2)
    print(account3)