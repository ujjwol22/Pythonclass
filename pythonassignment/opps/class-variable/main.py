# class attributes 
class item:
    pay_rent = 0.8 # they pay rate after 20% discount
    all = []
    
    def __init__(self, name:str, price:float, quantity = 0):
        # run validations to the received arguments 
        assert price >0, f'price {price} is not grater or equal to zero!'
        assert quantity >0, f'quantity {quantity} is not grater or equal to zero!'

        # assign to self object 
        self.name = name 
        self.price = price 
        self.quantity = quantity

        # actions to execute 
        item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rent

    def __repr__(self):
        return f"item('{self.name}', {self.price}, {self.quantity})"

item1 = item('phone', 100, 1)
item2 = item('laptop', 1000, 3)
item3 = item('cable', 10, 5)
item4 = item('mouse', 50, 5)
item5 = item('keyword', 75, 5)

print()
print(item.all)