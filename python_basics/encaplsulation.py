class Studentmarks:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return f"marks : {self.__marks}"
    def add_bonus(self,bonus):
        self.__marks+=bonus
        return f"marks after bonus : {self.__marks}"
    
a = Studentmarks("vivek", 89)
print(a.name)
print(a.get_marks())
print(a.add_bonus(3))

# print(a._Studentmarks__marks)  # ✅ This will work

