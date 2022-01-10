# syntxa of class methoda 
@classmethod
def method_name(clas): # => classmethod without parameters
    pass
    # statements

@classmethod
def metjod_name(cls, p1, p2): # => classmethod with parameters
    pass
    # statement


# class method without parameters 
class mobile:
    brand = 'Apple'
    price = 500000

    def name_price(self):
        print(f'the {self.brand} is {self.price}')

    @classmethod
    def full_name(cls):
        return f'{cls.brand}'

    @classmethod
    def brand_price(cls):
        return f'{cls.price}'

phone = mobile()
phone.name_price()
print(phone.full_name())
print(phone.brand_price())

print()
phone.brand = 'samsung'
phone.price = 'Rs: 400000'
phone.name_price
print(phone.full_name())
print(phone.brand_price())




# class method with parameters
print() 
class Mobile:
    brand = 'Vivo'
    price = None
    ram = None 

    @classmethod
    def full_name(cls):
        return f'{cls.brand}'

    @classmethod
    def phone_price_ram(cls, price, ram):
        cls.price = price
        cls.ram = ram
        return f'{cls.price} and {cls.ram}'

# objects 
phone = Mobile()
print(phone.full_name())
print(phone.phone_price_ram(10000, '4GB'))



# static method 
# syntxa 
@staticmethod
def method_name():
    pass
    # statmenet(s)

@staticmethod
def method_name():
    pass
    # statmenets(s)


# example 
print()
class Mobile:
    @staticmethod
    def show_model(model, price):
        model1 = model
        price1 = price 
        print(f'model: {model}')
        print(f'price: {price}')

phone = mobile()
Mobile.show_model('iphone 12 max-pro', '1,200,000|-')