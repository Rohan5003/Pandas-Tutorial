# class Vehicle:
#     def __init__(self,max_speed):
#         self.max_speed = max_speed
#     def show_speed(self):
#         return f" Max Speed : {self.max_speed}"
    
# class Bike(Vehicle):
#     def ride(self):
#         return "Riding the bike"
        
# b = Bike(80)
# print(b.show_speed())
# print(b.ride())

class A:
    def __init__(self):
        print("Class A init")

class B(A):
    def __init__(self):
        super().__init__()  # Call A's constructor
        print("Class B init")
  
c = B()

print(c)

