#OPP object oriented programming way 

#object - data, from which every logic will be executed in opr program

#Class - A blueprint which define objects

# ('name' , 'price')

class product:
    name ='projector'
    price = 10000
    quantity = 20

product1 = product()
print(product1.name , product1.price , product1.quantity)


class car:
    name = 'BMW'
    price = 5000000 
    top_speed = "200km/h"

    def get_name(self):
        print(self.name)

    def set_name(self, name):
        self.name = name
    
car1 = car()
#car1.get_name()

car1.set_name('Audi')
car1.get_name()

a = 'hello'.upper()
print(a)    


class car:
    name = 'BMW'
    price = 5000000 
    top_speed = "200km/h"

    car1 = car()
    print(car1.__dir__())    