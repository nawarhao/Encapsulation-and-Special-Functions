#public protected private in java
#privte __ syntax private. so that no one else, getter setter
class Car:

    def __init__(self, speed, color):
        self.__speed = speed
        self.__color = color
    
    #setter
    def set_speed(self,speed):
        self.__speed = speed
    #getter
    def get_speed(self):
        return self.__speed

car1 = Car(300, "orange")

# print(car1.__color) #this gives error as it is a private member
print(car1.get_speed())
car1.set_speed(400)
print(car1.get_speed())


