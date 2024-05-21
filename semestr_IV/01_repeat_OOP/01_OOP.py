#object Human <=> object Auto
# field (поле) or properties (властивість) => self.property   =>  action (дії)
class Human:
    def __init__(self,name="Human"):
        self.name=name

    def __str__(self):
        return f"Human's name is {self.name}"

class Auto:
    def __init__(self,brand) -> None:
        self.brand=brand
        self.passengers=[] # self.passengers=list()  => список людей (екземплярів Human) 

    # def add_passengers(self,human):
    #     self.passengers.append(human)
    
    def add_passengers(self,*humans):
        # print(humans)
        # print(type(humans))
        for passenger in humans:
            self.passengers.append(passenger)

    def print_passengers_names(self):
        if self.passengers!=[]:   #len(self.passengers>0)
            print(f"Names of {self.brand} passengers:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"There are no passengers in {self.brend}")
                
        


Alex=Human("Alex")
print(Alex.__class__)
print(type(Alex))
print(Alex.name)
Oleg=Human("Oleg")
print(Oleg)
print(Oleg.name)
Irina=Human("Irina")
# list1=list("Python")
# print(list1)
print("*"*30)
car=Auto("Mersedes")
print(car.brand)
print(car.passengers)
# add passangers
# car.add_passengers(Oleg)
# print(car.passengers)
# print(car.passengers[0])
# car.add_passengers(Alex)
# print(car.passengers)
# print(car.passengers[0].name, car.passengers[1].name)
car.add_passengers(Alex,Oleg)
car.print_passengers_names()
print("*"*30)
car_audi=Auto("Audi")
# car_audi.add_passengers(Oleg)
# car_audi.add_passengers(Irina)
car_audi.add_passengers(*[Oleg,Irina])
car_audi.print_passengers_names()
print("*"*30)
car_reno=Auto("Reno")
car_reno.add_passengers(Alex)
car_reno.print_passengers_names()