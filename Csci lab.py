class Account:
    def __init__(self, name = None, number = 0, balance = 0):
        self.name = name
        self.number = number
        self.balance = balance
    def print_info(self):
        print("Account Name: {}" .format(self.name))
        print("Account Number: {}" .format(self.number))
        print("Account Balance: ${}" .format(self.balance))
if __name__ == "__main__":
    account_details = Account()
    n = input()
    num = int(input())
    b = int(input())
    account_details.set_name(n)
    account_details.set_number(num)
    account_details.set_balance(b)
    account_details.print_info()