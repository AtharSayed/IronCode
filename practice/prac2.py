## Class and inheritance demo

class Car():
    # Setting the default constructor
    def __init__(self,model,color,mgyr):
        self.model = model
        self.color = color
        self.mgyr = mgyr

    ## Creating class method
    def design(self):
        print("\n1.The model of the car is",self.model,"it's",self.color,"and the manufacturing year is of ",self.mgyr)


# Inherited Class from parent class
class Sportcar(Car):

    def __init__(self,model,color,tpspeed):
        self.model = model
        self.color =color
        self.tpspeed =tpspeed

    # Method override with same function name as the above class
    def design(self):
        print("\n2. The car is ",self.model,"and its ",self.color,"with top-speed of ",self.tpspeed)

# Another inherited class from parent class

class truck(Car):

    def __init__(self,model,color,torq):
        self.model = model
        self.color = color
        self.torq = torq

    def design(self):
        print("\n3. The model is ",self.model,"with",self.color,"and a torque of ",self.torq)

if __name__ == "__main__":

    mycar =  Car("Hyundai","White",2013)

    mycar.design()

    # Creating  a new object of inherited class
    mynewcar = Sportcar("Ferrari","Red",450)

    mynewcar.design()

    mytrk = truck("Tata","Gold 407",340)
    mytrk.design()












