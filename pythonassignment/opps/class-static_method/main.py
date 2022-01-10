import csv
from os import read

class item:
    pay_rate = 0.8 # the pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity = 0):
        # run validations to the received arguments 
        assert price >= 0, f'price {price} is not greater than or equal to zero!'
        assert quantity >=0, f'Quantitu {quantity} is not greater than or ewual to zero!'

        # assign to self object 
        self.name = name 
        self.price = price 
        self.quantity = quantity
        
        # actions to execute 
        item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price =self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader) 

        for item in items:
            item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')) 
            )
    
    @staticmethod
    def is_integer(num):
        # we will count out the float that are point zero 
        # for i.e. 5.0, 10.0
        if isinstance(num, float):
            # count out the float that are point zero 
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f'item{self.name}, {self.price}, {self.quantity}'