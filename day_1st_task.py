def colculate_bmi(weight, hight):
    bmi=weight/hight
    return bmi


weight=float(input("enter weight value in kg : "))
height=float(input("enter height vealue in meter : "))

bmi=colculate_bmi(weight,height)
print(f"Bmi = {bmi:.3f}")

if bmi < 18:
    print ("Your are under height")
elif bmi>18 and bmi <=24:
    print ("Your are heigher ")
elif bmi >24 and bmi <= 29:
    print("Your heighest")
else:
    print("Your are abese")