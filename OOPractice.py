class Dog():
    
    def __init__(self,breed,name,tail):

        #attributes 
        #take in argument
        #assign using self.attribute_name
        self.breed = breed
        self.name = name

        #expected boolean
        self.tail = tail

my_dog = Dog(breed='Malamute',name='Thor',tail=True)
type(my_dog)

print([my_dog.breed,my_dog.name,my_dog.tail])
