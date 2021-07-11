weight = float(input("Enter your weight in kilograms:"))
height = float(input("Enter your height in meters:"))

bmi = weight/(height**2)

if bmi <= 18:
    print("Underweight")
elif bmi >= 19 and bmi <= 24:
    print("Normal weight")
elif bmi >= 25 and bmi <= 29:
    print("Overweight")
else:
    print("Obese")