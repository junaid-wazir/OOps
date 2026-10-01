# ==========================================
# Task : Item Class & Test Code
# ==========================================


class Item:

  def __init__(self, item_name, item_quantity, item_price, tax_rate):
    self.item_name = item_name
    self.item_quantity = item_quantity
    self.item_price = item_price
    self.tax_rate = tax_rate  # Tax rate percentage mein (e.g., 5 for 5%)

  # Tax calculate karne ka method
  def calculate_tax(self):
    return (self.item_price * self.tax_rate / 100) * self.item_quantity

  # Total price calculate karne ka method (Price + Tax)
  def calculate_total_price(self):
    subtotal = self.item_price * self.item_quantity
    return subtotal + self.calculate_tax()

  # Print format ke liye __str__ method
  def __str__(self):
    return (
        f"Item Name: {self.item_name} | Quantity: {self.item_quantity} | "
        f"Unit Price: ${self.item_price:.2f} | Tax: ${self.calculate_tax():.2f} | "
        f"Total: ${self.calculate_total_price():.2f}"
    )


# Item Class ke Test Cases
print("--- ITEM CLASS DETAILS ---")
item1 = Item("Laptop", 2, 1200.0, 5.0)  # 5% tax
item2 = Item("Mouse", 5, 25.0, 10.0)  # 10% tax

print(item1)
print(item2)
print()



# Task : Date Class & Test Code



class Date:

  def __init__(self, day, month, year):
    self.day = day
    self.month = month
    self.year = year

  # Day/Month/Year Format ke liye __str__ method
  def __str__(self):
    return f"{self.day:02d}/{self.month:02d}/{self.year}"


# Date Class ka Test Case
print("--- DATE CLASS DETAILS ---")
date1 = Date(1, 10, 2026)
print(f"Formatted Date: {date1}")