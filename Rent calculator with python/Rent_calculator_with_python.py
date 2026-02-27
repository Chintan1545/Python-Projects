## Rent calculator with python

rent = int(input("Enter your total rent: "))
food = int(input("Enter the amount of food ordered: "))
ele_spend = int(input("Enter the total electricity units consumed: "))
charge_per_unit = int(input("Enter the charge per unit: "))
persons = int(input("Enter the number of persons living: "))

total_bill = ele_spend * charge_per_unit
total_expense = rent + food + total_bill

output = total_expense / persons

print("Each person will pay:", round(output, 2))


## output 
'''
Enter your total rent:  5000
Enter the amount of food ordered:  2000
Enter the total electricity spend:  300
Enter the charge per unit:  10
Enter the number of person living:  3
Each person will pay:  3333
'''