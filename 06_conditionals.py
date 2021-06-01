# if statements
# comparison operators

salary = 2000

if salary < 1000:
    print("Under Paid")
elif(salary == 2000):
    print("Well Paid")
else:
    print("Over Paid")

print("Salary STATEMENT")


# The price of a house is $1M
# if a buyer has good credit  - they need a down payment of 10%
# otherwise 20%
price = 1000000

has_good_credit = True

if has_good_credit:
    downpayment = 0.1*price
else:
    downpayment = 0.2*price

print(f"Down Payment: ${downpayment}")


# Logical Operators
# build a program to process loans -
# Version 1
# if an applicant has high income and good credit then they are eligible for a loan
has_good_credit = True
has_high_income = True

if has_good_credit and has_high_income:
    print("Eligible")


# Version 2
# if an applicant has high income or good credit then they are eligible for a loan
has_good_credit = True
has_high_income = False

if has_good_credit or has_high_income:
    print("Eligible")

# Version 3

# if an applicant has a good credit and does not have a criminal record then they are eligible for a loan
has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("Eligible")


# write a program to convert a users input from kgs to lbs and vice-versa
weight = int(input("Weight:  "))
unit = input("(L)bs or K(g)s  ")

if(unit.upper() == "L"):
    converted = weight*0.45
    print(f"You are {round(converted, 2)} Kilos")
else:
    converted = weight/0.45
    print(f"You are {round(converted, 2)} pounds")
