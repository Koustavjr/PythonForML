class Car:
    car_count=0
    def __init__(self,brand,model):
        self.__brand=brand  #private
        self.__model=model
        self.car_count+=1
        Car.car_count+=1
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    def get_brand(self):
        return self.__brand
    
    def description(self):
        return "Petrol or Diesel car"
    @staticmethod
    def useage():
        return "Cars are means of transport"
    @property
    def get_model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self,brand,model,battery):
        super().__init__(brand,model)
        self.battery=battery
    def description(self):
        return "Electric Battery car"
        


#car1=Car("tata","nano")

# #print(car1.brand) #cannot be accessed as private
# #print(car1.__brand)
# print(car1.get_brand())
# print("Full name: ",car1.full_name())
# print(car1.description())


# electricCar1=ElectricCar("Tesla","Neon","85Kwh")

# #print(electricCar1.model,electricCar1.battery)
# print(electricCar1.description())

# print("Total car count by instance ",car1.car_count)
# print("Total car count by class ",Car.car_count)

# print(car1.useage())
# print(electricCar1.useage())

#modifying model attribute

car2=Car("Tata","Safari")
#print(car2.__model)
print(car2.get_model)
car2.__model="City" # doesnot modify
# car2.get_model="city" throws error
#print(car2.__model)
print(car2.get_model)

print(isinstance(car2,Car))
print(isinstance(ElectricCar,Car))

# multiple inheritance
class Battery:
    def battery_info(self):
        return "90kwh" 

class Engine:
    def engine_info(self):
        return "Toyota Engine"

class ElectricCarTwo(Battery,Engine,ElectricCar):
    pass

electricCar=ElectricCarTwo("Toyota","Corola","85kwh")
print(electricCar.battery_info())
print(electricCar.engine_info())
print(electricCar.battery)


class Bike:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

class bike2(Bike):
    def __init__(self,brand,model,battery):
        super().__init__(brand,model)
        self.battery=battery

class bike3(Bike):
    pass

b1=bike2("KTM","X2","50kwh")
print(b1.brand,b1.model,b1.battery)

b2=bike3("KTM","X3")
print(b2.brand,b2.model)