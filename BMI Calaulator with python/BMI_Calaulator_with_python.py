## BMI Calaulator with python

height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight kg: "))

height = height / 100
BMI = weight / (height * height)
print("Your body masa index is: ",BMI)

if BMI > 0:
    if BMI <= 16:
        print("You are severely underweight")
    elif BMI <= 18.5:
        print("You are underweight")
    elif BMI <= 25:
        print("You are healthy")
    elif BMI <= 30:
        print("You are overweight")
    else:
        print("You are severely overweight")
else:
    print("Enter valid details")


## output
'''
Enter your height in cm:  166
Enter your weight kg:  75
Your body masa index is:  27.21730294672667
You are overweight
'''