class Inventory_item:
    def __init__(self, desc, cost, quantity):
        self.description = desc
        self.cost = cost
        self.quantity = quantity

    def __str__(self):
        return 'Description: %s, Cost: $%.2f, Quantity: %d' % (self.description, self.cost, self.quantity)


def main():
    inventory_list = [Inventory_item("item 1", 100, 2), Inventory_item("item 2", 55, 9), Inventory_item("item 3", 23, 7)]
    for item in inventory_list:
        print(item)

main()