class Item:
    """
    This class contains items details
    """ 
    pay_rate = 10

    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.total = 0 

    def calculate_total_price(self):
        self.total = self.price * self.quantity
        return self.total
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}','{self.price}','{self.quantity}')"


item1 = Item()
item1.calculate_total_price()
