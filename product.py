class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    def update_price(self, percent_change):
        if percent_change>0:
            self.price+=(percent_change*self.price)/100
        else:
            self.price+=(percent_change*self.price)/100
        return self

    def print_info(self):
        print(self.name)
        print(self.price)
        print(self.category)
        return self
        
if __name__ == "__main__":
    football = Product("football", 25.99, "sports")
    football.print_info().update_price(-10).print_info()
