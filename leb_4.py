"""class date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

class product:
    def __init__(self, name, price, purchasing_date):
        self.name = name
        self.price = price
        self.purchasing_date = purchasing_date
    def __set__(self):
        return f"Product Name: {self.name}, Price: ${self.price}, Purchasing Date: {self.purchasing_date}"

d1=date(2023, 6, 1)
d2=date(2023, 6, 10)

p1=product("Laptop", 1200, d1)
p2=product("Smartphone", 800, d2)
print(p1)
print(p2) """

"""
Create an Item class with the variables for the item name, item quantity and item price
and tax rate. The objects should be initialized through constructor. Use a str method in
the class to print each object in a consistent format. Use methods/functions to calculate
the tax and price.
"""

# initializing object whith default values
from operator import gt


class student :
    def __init__(self,name ,student_id, age=0,gread ="Not Specified"):
        self.name = name #required parameter
        self.student_id = student_id #required parameter
        self.age = age#optional parameter with default value
        self.gread = gread#optional parameter with default value
    def __str__(self):
        return f"Name: {self.name}, Student ID: {self.student_id}, Age: {self.age}, Gread: {self.gread}"

s1 = student("John", "S12345", 20, "A")
s2 = student("Alice", "S67890", 19)
s3 = student("Bob", "S54321",gread="B")
print(s1.name)
print(s1.student_id)
print(s1.age)
print(s1.gread)
print(s2.name)
print(s2.student_id)
print(s2.age)
print(s2.gread)
print(s3.name)
print(s3.student_id)
print(s3.age)
print(s3.gread)