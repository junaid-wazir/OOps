class student :
    def study(self , name ):
        print(f"{name} is studying.")

student1 = student()
name = input("Enter the name of the student: ")
student1.study(name)
