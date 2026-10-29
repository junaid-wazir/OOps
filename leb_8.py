
class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    def displayDate(self):
        return f"{self.day:02d}-{self.month:02d}-{self.year}"

    def __str__(self):
        return self.displayDate()


class Student:

    noOfStudents = 0

    def __init__(self, studentNo="not known",studentName="not known",dateOfBirth=None, meritPoints=20):

        self.studentNo = studentNo
        self.studentName = studentName

        if dateOfBirth is None:
            self.dateOfBirth = Date()
        elif isinstance(dateOfBirth, Date):
            self.dateOfBirth = dateOfBirth
        else:
            self.dateOfBirth = Date()

        self.setMeritPoints(meritPoints)

        Student.noOfStudents += 1

    def setStudentNo(self, studentNo):
        self.studentNo = studentNo

    def setStudentName(self, studentName):
        self.studentName = studentName

    def setDateOfBirth(self, dateOfBirth):
        if isinstance(dateOfBirth, Date):
            self.dateOfBirth = dateOfBirth
        else:
            print("Invalid date object.")

    def setMeritPoints(self, meritPoints):
        if isinstance(meritPoints, int) and 20 <= meritPoints <= 200:
            self.meritPoints = meritPoints
        else:
            self.meritPoints = 20
            print("Invalid merit points! Default value 20 assigned.")

    def getStudentNo(self):
        return self.studentNo

    def getStudentName(self):
        return self.studentName

    def getDateOfBirth(self):
        return self.dateOfBirth

    def getMeritPoints(self):
        return self.meritPoints

    def displayStudent(self):
        print("Student Number:", self.studentNo)
        print("Student Name:", self.studentName)
        print("Date of Birth:", self.dateOfBirth)
        print("Merit Points:", self.meritPoints)


class Undergraduate(Student):

    def __init__(self, studentNo="not known",
                 studentName="not known",
                 dateOfBirth=None, meritPoints=20,
                 testScore=0):

        super().__init__(
            studentNo, studentName, dateOfBirth, meritPoints
        )
        self.testScore = testScore

    def calculateMerit(self):
        return self.meritPoints + self.testScore

    def displayStudent(self):
        super().displayStudent()
        print("Test Score:", self.testScore)
        print("Overall Merit:", self.calculateMerit())


class Postgraduate(Student):

    def __init__(self, studentNo="not known",
                 studentName="not known",
                 dateOfBirth=None, meritPoints=20,
                 GPA=0.0):

        super().__init__(
            studentNo, studentName, dateOfBirth, meritPoints
        )
        self.GPA = GPA

    def calculateMerit(self):
        return self.meritPoints + self.GPA

    def displayStudent(self):
        super().displayStudent()
        print("GPA:", self.GPA)
        print("Overall Merit:", self.calculateMerit())



student1 = Student()

student2 = Student(
    "101", "Ali", Date(12, 3, 2005), 100
)

student3 = Undergraduate(
    "102", "Ahmad", Date(10, 5, 2004), 120, 60
)

student4 = Postgraduate(
    "103", "Usman", Date(15, 8, 2000), 100, 3.5
)


print("\n--- Student 1 ---")
student1.displayStudent()

print("\n--- Student 2 ---")
student2.displayStudent()

print("\n--- Undergraduate Student ---")
student3.displayStudent()

print("\n--- Postgraduate Student ---")
student4.displayStudent()

print("\nTotal Students:", Student.noOfStudents)
