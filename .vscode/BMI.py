print ("--- 2026 Health Analyzer ---")

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))

bmi = weight / ((height / 100) ** 2)
print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    status = "Underweight"
elif 18.5 <= bmi < 24.9:
    status = "Normal weight"
elif 25 <= bmi < 29.9:
    status = "Overweight"
elif 30 <= bmi < 34.9:
    status = "Obese"
else:
    status = "Severely obese"

print("-"*30)
print(f"Result: {status} ({bmi:.2f})")