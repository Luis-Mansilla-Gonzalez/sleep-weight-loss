import math

sex = input("Please type sex assigned at birth, M/F ").strip().upper()
weight = int(input("Weight in pounds: "))
height = int(input("Height in inches: "))
age = int(input("Age: "))
pounds = int(input("How many pounds do you want to lose? "))

if sex == "M":    
    bmr = 66 + (6.2 * weight) + (12.7 * height) - (6.76 * age)
    
elif sex == "F":
    bmr = 655.1 + (4.35 * weight) + (4.7 * height) - (4.7 * age)
    
else:
    print("Invalid input (working on future additions!)")
    exit()
    
cal_hour = bmr/24
calories = 3500 * pounds
sleep = calories/cal_hour
print(f"In order to lose {pounds} pounds, you need to sleep for {sleep} hours")
