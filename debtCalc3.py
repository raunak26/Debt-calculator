# program.py
# Raunak Anand
# ECS32A Fall 2018
# 17 October 2018
# This code calculates your monthly compound interest over regualar intervals. 

from inputCheck import canBeFloat

Debt = input("Enter amount of debt:") # initial debt
interest_rate = input("Enter % interest rate:")  # interest_rate is Interest Rate in %
monthly_payment = input("Enter monthly payment:")  # monthly_paymnet is Monthly payment in dollars ($)

month = 1
total_payment = 0

if canBeFloat(Debt) != True: # if debt is not a float
    print("Bad input, enter a number next time.")
    print("Press enter to exit")
elif canBeFloat(interest_rate) != True: # if interest rate is not a float
    print("Bad input, enter a number next time.")
    print("Press enter to exit")
elif canBeFloat(monthly_payment) != True: # if monthly installment is not a float
    print("Bad input, enter a number next time.")
    print("Press enter to exit")
else:
    Debt = float(Debt) # converting Debt to float
    interest_rate = float(interest_rate) # converting interest rate to float as we did with Debt
    monthly_payment = float(monthly_payment) # converting monthly_payment to float
    if monthly_payment <= interest_rate:
        print("You will need to make bigger payments.\nAt this rate you will never pay off the debt.\nPress enter to exit")
    else:
        while Debt >= monthly_payment:
            print("Month =",month) # number of months
            monthly_interest = Debt * (interest_rate / 1200) # monthly_interest is the monthly interest in %
            Debt = Debt - monthly_payment + monthly_interest # forward balance after monthly installment is paid
            total_payment = total_payment + monthly_payment
            print("Interest this month =","%.2f" % monthly_interest)
            print("Balance going forward =","%.2f" % Debt) # outstanding balance left to pay
            print("Total payments =","%.2f" % total_payment) # monthly installment
            month = month + 1

        print("Month =",month)
        monthly_interest = Debt * (interest_rate / 1200)
        print("Interest this month =","%.2f" % monthly_interest)
        print("Balance going forward = 0.00")
        print("Total payments =","%.2f" % (total_payment + monthly_interest + Debt))
        print("Press enter to exit")
    
