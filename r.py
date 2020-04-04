class Total:
    def __init__(self, item = "None", num=0, price=0):
        self.name = item
        self.quantity = num
        self.price = price

    def print_info(self):
        print("TOTAL COST")
        for i in range(0,2):
            print("{} {} @ ${} = ${}".format(self.name[i], self.quantity[i], self.price[i], (self.price[i] * self.quantity[i])))
        print("Total: ${}".format((self.price[0] * self.quantity[0]) + (self.price[1] * self.quantity[1]))

if __name__ == "__main__":
    set_name = []
    set_price = []
    set_quantity = []
    price_t = Total(set_name,  set_quantity, set_price)
    i = 1
    while i <= 2:
        print("Item{}" .format(i))
        set_name.append(input("Enter the item name:\n"))
        set_price.append(int(input("Enter the item price:\n")))
        set_quantity.append(int(input("Enter the item quantity:\n")))
        i += 1
price_t.print_info()