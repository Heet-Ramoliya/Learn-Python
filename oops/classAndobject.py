class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"{self.brand} {self.model}"

mycar = Car("Tata","Safari")

print(mycar.model)
print(mycar.brand)
print(mycar.full_name())



