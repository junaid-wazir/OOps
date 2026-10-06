class employee:
    def __init__(self, emp_id, emp_name, sel1=0, sel2=0, sel3=0):
        self.__emp_id = emp_id
        self.__emp_name = emp_name
        self.__sel1 = sel1
        self.__sel2 = sel2
        self.__sel3 = sel3
    def average_sales(self):
        return (self.__sel1 + self.__sel2 + self.__sel3) / 3
    def __str__(self):
        sel=f"{self.__sel1}, {self.__sel2}, {self.__sel3}"
        return (f"ID: {self.__emp_id}\n"
                f"Name: {self.__emp_name}\n"
                f"Sales: {sel}\n"
                f"Average Sales: {self.average_sales():.2f}")
def read_employee(n):
    print(f"Enter details for employee {n}:")
    emp_id = int(input("Enter employee ID: "))
    emp_name = input("Enter employee name: ")
    sel1 = float(input("Enter sales for month 1: "))
    sel2 = float(input("Enter sales for month 2: "))
    sel3 = float(input("Enter sales for month 3: "))
    return employee(emp_id, emp_name, sel1, sel2, sel3)

emp1=read_employee(1)
emp2=read_employee(2)

print("\n--- Employee 1 Details ---")
print(emp1)
print("\n--- Employee 2 Details ---")
print(emp2)