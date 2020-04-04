class Total:
    def __init__(self, item = "None", num=0, price=0):
        self.item_name = item
        self.item_quantity = num
        self.item_price = price

    def print_info(self):
        print("TOTAL COST")
        for i in range(0,2):
            print("{} {} @ ${} = ${}".format(self.item_name[i], self.item_quantity[i], self.item_price[i], (self.item_price[i] * self.item_quantity[i])))
        print("Total: ${}".format((self.item_price[0] * self.item_quantity[0]) + (self.item_price[1] * self.item_quantity[1])))

if __name__ == "__main__":
    set_item_name = []
    set_item_price = []
    set_item_quantity = []
    price_t = Total(set_item_name,  set_item_quantity, set_item_price)
    i = 1
    while i <= 2:
        print("Item{}" .format(i))
        set_item_name.append(input("Enter the item name:\n"))
        set_item_price.append(int(input("Enter the item price:\n")))
        set_item_quantity.append(int(input("Enter the item quantity:\n")))
        i += 1
price_t.print_info()