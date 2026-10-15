"""
class book:
    def __init__(self, title, author, price):
        self.__title = title
        self.__author = author
        self.__price = price

    def display_info(self):
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")
        print(f"Price: ${self.__price:.2f}")

    def __str__(self):
        return f"Title: {self.__title}\nAuthor: {self.__author}\nPrice: ${self.__price:.2f}"

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author
    def get_price(self):
        return self.__price
    def set_title(self, title):
        self.__title = title
    def set_author(self, author):
        self.__author = author
    def set_price(self, price):
        self.__price = price
if __name__ == "__main__":
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    price = float(input("Enter the book price: "))

    book1 = book(title, author, price)
    print("\n--- Book Details ---")
    print(book1)

    new_price = float(input("Enter the new price: "))
    book1.set_price(new_price)
    print("\n--- Updated Book Details ---")
    print(book1)"""

#Doosre sawal ke mutabiq do mobiles ka data, private variables, set/get methods aur price update ka code yeh raha[cite: 1]:
class mobile:
    def __init__(self, brand, model, price):
        self.__brand = brand
        self.__model = model
        self.__price = price
    def get_brand(self):
        return self.__brand
    def get_model(self):
        return self.__model
    def get_price(self):
        return self.__price
    def set_brand(self, brand):
        self.__brand = brand
    def set_model(self, model):
        self.__model = model
    def set_price(self, price):
        self.__price = price

print("Enter details for Mobile 1:")
b1 = input("Enter brand: ")
m1 = input("Enter model: ")
p1 = float(input("Enter price: "))
mobile1 = mobile(b1, m1, p1)

print("\nEnter details for Mobile 2:")
b2 = input("Enter brand: ")
m2 = input("Enter model: ")
p2 = float(input("Enter price: "))
mobile2 = mobile(b2, m2, p2)

print("\n--- Mobile 1 Details ---")
print(f"Brand: {mobile1.get_brand()}")
print(f"Model: {mobile1.get_model()}")
print(f"Price: ${mobile1.get_price():.2f}")

print("\n--- Mobile 2 Details ---")
print(f"Brand: {mobile2.get_brand()}")
print(f"Model: {mobile2.get_model()}")
print(f"Price: ${mobile2.get_price():.2f}")

new_p1 = float(input("\nEnter new price for Mobile 1: "))
mobile1.set_price(new_p1)

new_p2 = float(input("Enter new price for Mobile 2: "))
mobile2.set_price(new_p2)


class student:
    def __init__(self, reg_no,name, gpa):
        self.__reg_no = reg_no
        self.__name = name
        self.__gpa = gpa
    def display_details(self):
        print(f"Registration Number: {self.__reg_no}")
        print(f"Name: {self.__name}")
        print(f"GPA: {self.__gpa:.2f}")
    def get_reg_no(self):
        return self.__reg_no
    def get_name(self):
        return self.__name
    def get_gpa(self):
        return self.__gpa
    def set_reg_no(self, reg_no):
        self.__reg_no = reg_no
    def set_name(self, name):
        self.__name = name
    def set_gpa(self, gpa):
        self.__gpa = gpa
    def __str__(self):
        return f"Registration Number: {self.__reg_no}\nName: {self.__name}\nGPA: {self.__gpa:.2f}"

user1=student(input("Enter registration number: "),
              input("Enter name: "),
              float(input("Enter GPA: ")))
print(user1)

new_gpa=float(input("Enter new GPA: "))
user1.set_gpa(new_gpa)
print(user1)