"""
Exercise 03:
Write a computer program offer_loan.py to implement the following specification: 
A bank will offer a customer a loan if they are 21 or over, have an annual income of at least £21000 and has not received a loan in the past. 
The program takes in input from the user the customer’s age, their income and whether they have received a loan already. 
The program outputs the string “The loan can be offered: True” if the conditions are met, otherwise ”The loan can be offered: False”.

*Hints: bool() is the type casting function for converting to a boolean type.

"""

# calling for user inputs
age = int(input("What is your age: "))
annual_income = float(input('what is your annual income :'))
loan_status =bool(input('have you received a loan before? :'))


## testing conditions to offer loan
if age>=21 and annual_income >=21000 and loan_status == True:
    print('The loan can be offered: True')

else:
    print("The loan can be offered: False")
    