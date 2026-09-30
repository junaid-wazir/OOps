class date:
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
print(p2)