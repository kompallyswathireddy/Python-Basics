height = float(input("Enter your height in cm: "))  # Input height in cm
weight = float(input("Enter your weight in kg: "))  # Input weight in kg

# Convert height from cm to meters and calculate BMI
BMI = weight / (height / 100) ** 2

# Output the calculated BMI
print("Your BMI is", round(BMI, 2))

# Classify the BMI result
if BMI < 18.5:
    print("You are underweight.")
elif 18.5 <= BMI <= 24.9:
    print("You are healthy.")
elif 25 <= BMI <= 29.9:
    print("You are overweight.")
elif 30 <= BMI <= 34.9:
    print("You are severely overweight.")
elif 35 <= BMI <= 39.9:
    print("You are obese.")
else:
    print("You are severely obese.")