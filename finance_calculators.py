#Compulsory Task 1
#This is the first capstone project from HyperionDev DS bootcamp
#Financial calculators for investment and home loan repayment
#Check if entered invalid calcalator return error message

import math
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")
print("")
calculator_option = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
print("")

if calculator_option.lower() == "investment":
    print("investment calculator:\n")
    deposit = float(input("Please enter the amount of money you are depositing: "))
    interest_rate = float(input("Please enter the interest rate in (%): "))
    year = float(input("Please enter the number of years you plan on investing: "))
    interest = input("Please choose 'simple' or 'compound' interest: ")

    if interest.lower() == "simple":
        amount_simple = deposit * (1 + (interest_rate/100) * year)
        format_amount_simple = round(amount_simple, 3)
        print(f"The amount you will get back after {year} year(s) is ${format_amount_simple}")

    elif interest.lower() == "compound":
        amount_compound = deposit * math.pow((1 + (interest_rate / 100)),year)
        format_amount_compound = round(amount_compound, 3)
        print(f"The amount you will get back after {year} year(s) is ${format_amount_compound}")

elif calculator_option.lower() == "bond":
    print("bond calculator:\n")
    present_value = float(input("Please input the present value of the house: "))
    interest_bond = float(input("Please enter the interest rate in (%): "))
    rate = interest_bond/100
    months = float(input("Please enter the number of months you plan to take to repay the bond: "))
    repayment = ((rate/12) * present_value)/(1 - (1 + (rate/12))**(-months))
    format_repayment = round(repayment, 3)
    print(f"The amount you will have to repay each month is ${format_repayment}")

else:
    print("Sorry you've entered an invalid input.")


