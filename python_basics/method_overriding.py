class Employee:
    def work(self):
        return f"works {9} to {5}"
    
class Freelancer(Employee):
    def work(self):
        return "works flexible hours"
    
z = Employee()
y = Freelancer()

print(z.work())
print(y.work())