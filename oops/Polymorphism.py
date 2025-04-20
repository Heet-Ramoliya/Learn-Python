class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + "!"
    
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fule_type(self):
        return "Petrol and Diesel"
    
class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fule_type(self):
        return "Electric charger"

my_tesla = ElectricCar("Tesla","Model s","85kwh")
my_car = Car("Tata","Safari")

print(my_tesla.fule_type())
print(my_car.fule_type())


