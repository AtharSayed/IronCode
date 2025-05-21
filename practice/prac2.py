## Class and inheritance demo

class Car():
    # Setting the default constructor
    def __init__(self,model,color,mgyr):
        self.model = model
        self.color = color
        self.mgyr = mgyr

    ## Creating class method
    def design(self):
        print("The model of the car is",self.model,"it's",self.color,"and the manufacturing year is of ",self.mgyr)



if __name__ == "__main__":
    mycar =  Car("Hyundai","White",2013)
    mycar.design()







