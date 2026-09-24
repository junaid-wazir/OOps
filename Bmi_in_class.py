class BmiCalculator:
    def calculate_bmi(self, weight:int, height:float):
        bmi = weight / (height ** 2)
        print (f"The BMI is: {bmi:.2f}")
        if bmi < 18:
            print("You are underweight.")
        elif bmi < 25:
            print("You have a normal weight.")
        else:
            print("You are overweight.")

weight = int(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi_calculator = BmiCalculator()
bmi_calculator.calculate_bmi(weight, height)