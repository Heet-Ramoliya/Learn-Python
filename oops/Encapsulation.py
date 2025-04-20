class Car:
    def __init__(self,brand,model):
        # __brand is private attributes
        self.__brand = brand
        self.model = model

    # this function use of get private brand name
    def get_brand(self):
        return self.__brand + "!"
    
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla","Model s","85kwh")

print(my_tesla.get_brand())
# this brand is not direct access therefor use above get_brand function
# print(my_tesla.__brand)
print(my_tesla.model)
print(my_tesla.full_name())
print(my_tesla.battery_size)

