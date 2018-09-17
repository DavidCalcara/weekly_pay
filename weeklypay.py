"""
Program: weeklypay.py
Author: David
Calculate and output the employees total weekly pay
"""
# Request the inputs
hourlyWage = int(input("Hourly wage?"))
totalRegularHours = int(input("Total regular hours?"))
totalOvertimeHours = int(input("Total overtime hours?"))

# Compute the total weekly pay
overtime = int(totalOvertimeHours * float(1.5 * hourlyWage))
totalWeeklyPay = ((hourlyWage * totalRegularHours) + overtime)

# Display the result
print("Your weekly pay is $", str(totalWeeklyPay))