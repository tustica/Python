import random
from product import Product

class Store:
    def __init__(self, name):
        self.name = name
        self.list_of_products = []

    def add_product(self, name, price, category):
        self.list_of_products.append(Product(name, price, category))
        for attr, vals in self.list_of_products[len(self.list_of_products)-1].__dict__.items():
            print(attr,": ", vals)
        return self

    def sell_product(self, ID):
        for x in range(len(self.list_of_products)-1):
            if self.list_of_products[x]['id'] == ID:
                self.list_of_products.pop()
        print(self.list_of_products)

    def inflation(self, percent_increase):
        for items in self.list_of_products:
            items.update_price(percent_increase)
            print("After inflation of",str(percent_increase)+"%", "the new price for the",items.name, " is ",items.price)
    
    def set_clearance(self, cateogry, percent_discount):
        for items in self.list_of_products:
            if items.category == cateogry:
                items.update_price(percent_discount)
                print("With the discount, the",items.name,"is now",items.price)
            else:
                print('category does not exist')

    def print_store_info(self):
        print(self.list_of_products)

nesher = Store("Nesher")
nesher.add_product("football", 25, "sports")
nesher.add_product("soccer ball", 15, "sports")
nesher.inflation(7)
nesher.set_clearance("sports", -10)


