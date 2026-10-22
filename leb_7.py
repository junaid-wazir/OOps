class course:
    def __init__(self, name, credits, card_hours):
        self.name = name
        self.credits = credits
        self.card_hours = card_hours
    def display_details(self):
        print(f"Course Name: {self.name}")
        print(f"Credits: {self.credits}")
        print(f"Card Hours: {self.card_hours}")

    def get_name(self):
        return self.name
    def get_credits(self):
        return self.credits
    def get_card_hours(self):
        return self.card_hours
    def set_name(self, name):
        self.name = name
    def set_credits(self, credits):
        self.credits = credits
    def set_card_hours(self, card_hours):
        self.card_hours = card_hours
    def __str__(self):
        

# main program
print("Enter details for Course 1:")
course1 = course(input("enter course name: "),
int(input("enter course credits: ")),
int(input("enter course card hours: ")))
print("\nCourse 1 Details:")
course1.display_details()
print(course1)

class faculty:
    def __init__(self, name, monthly_salary, course=1):
        self.name = name
        self.monthly_salary = monthly_salary
        self.course = course
        self.course = course()
        if self.course.credits >12:
            self.monthly_salary = self.monthly_salary + 2800
    def display_details(self):
        print(f"Faculty Name: {self.name}")
        print(f"Monthly Salary: {self.monthly_salary}")
        print(f"Course: {self.course}")

    def get_name(self):
        return self.name
    def get_monthly_salary(self):
        return self.monthly_salary
    def get_course(self):
        return self.course
    def set_name(self, name):
        self.name = name
    def set_monthly_salary(self, monthly_salary):
        self.monthly_salary = monthly_salary
    def set_course(self, course):
        self.course = course
     def __str__(self):
        return f"Faculty Name: {self.name}, Monthly Salary: {self.monthly_salary}, Course: {self.course}"

# main program
print("\nEnter details for Faculty:")
faculty1 = faculty(input("Enter faculty name: "),
float(input("Enter monthly salary: ")), course1)
print("\nFaculty Details:")
faculty1.display_details()
print(faculty1)


class client:
    def __init__(self):
        self.__course = course()
        self.__faculty=faculty()

# main program
c1=client()
print(c1)