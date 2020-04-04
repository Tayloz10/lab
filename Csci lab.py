class Account:
    account1_name = "Trish Duce"
    account1_number = 90453889
    account1_balance = 100.00
    account2_name = "Donald Duck"
    account2_number = 74773321
    account2_balance = 100.00
    account3_name = "Joe Smith"
    account3_number = 74773321
    account3_balance = 150.00
    def __init__(self, name = None, number = 0, balance = 0):
        self.name = name
        self.number = number
        self.balance = balance
    def print_info(self):
        print("Account Name: {}" .format(self.name))
        print("Account Number: {}" .format(self.number))
        print("Account Balance: ${}" .format(self.balance))
if __name__ == "__main__":
   account1 = Account
   account2 = Account
   account3 = Account
   account2.print_info
   account2.print_info
   account2.print_info