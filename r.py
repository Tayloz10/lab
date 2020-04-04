class Total:
    def __init__(self, item = "None", num=0, price=0):
        self.name = item
        self.quantity = num
        self.price = price

    def print_info(self):
        print("TOTAL COST")
        for i in range(2):
            print("{} {} @ ${} =${}".format(self.name[i], self.quantity[i], self.price[i], (self.price[i] * self.quantity[i])))
            print("Total: ${}".format(self.price[i] * self.quantity[i]))

if __name__ == "__main__":
    price_t = Total()
    price_t.set_name = []
    price_t.set_price = []
    price_t.set_quantity = []
    i = 1
    while i <= 2:
        print("Item{}" .format(i))
        price_t.set_name = input("Enter the item name:\n")
        price_t.set_price = int(input("Enter the item price:\n"))
        price_t.set_quantity = int(input("Enter the item quantity:\n"))
        i += 1
price_t.print_info()
