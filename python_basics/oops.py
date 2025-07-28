# class car:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year

# c = car("lexus",2003)

# print(c.brand)
# print(c.year)

# class mobile:
#     def __init__(self, model, price):
#         self.model = model
#         self.price = price

# m = mobile("apple", 150000)
# print(m.model)
# print(m.price)

# class Rectangle :
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth

#     def area(self):
#         return  self.length * self.breadth

# r = Rectangle(5,2)

# print(r.area())

# class Book:
#     def __init__(self,title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def description(self):
#         return f"Book : {self.title} by {self.author}, {self.pages} pages"

# b = Book("python", "Rohan", 400)
# print(b.description())


class Student:
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks
    
    def grade(self):
        if(self.marks>=90 and self.marks<=100):
            return "A"
        elif(self.marks>=80 and self.marks<=89):
            return "B"
        elif(self.marks>=70 and self.marks<=79):
            return "C"
        else:
            return "FAIL"
        
s = Student("Vivek",99)
print(s.grade())

    
