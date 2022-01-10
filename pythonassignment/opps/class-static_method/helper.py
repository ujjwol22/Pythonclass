# when to use class method and when to use static method ?
class items:
    @staticmethod
    def is_intiger():
        '''
        This should do soething that has a relationship
        with the class, but not something that must be unique per instance!
        '''
    @classmethod
    def instance_form_something(cls):
        '''
        This should also do somthing that has a relationship 
        with the class, but usually, those are used to manipulate differerent structure of data to instantiate objects, like we have done with CSV.
        '''

# the only difference between those :
# static mrthod are not passing the object reference as the fist arguments in the background

# Note: however, those could be also called frominstances 
item1 = items()
print(item1.is_intiger())
print(item1.instance_form_something())