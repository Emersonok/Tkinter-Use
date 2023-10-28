
def add(*args):
    print(sum(args))

#num = int(input("Write num "))
#num2 = int(input("Write num "))
add(4, 5, 6, 7, 10, 15)

class Car:
    def __init__(self,  **kw):
        self.color = kw.get("color")
        self.model = kw.get("model")
        self.year = kw.get("year")
        

my_car = Car(color="Red")
print(my_car.color)

        