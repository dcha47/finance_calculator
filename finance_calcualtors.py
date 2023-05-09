import math

# this a python program to calculate a users interest on an ivestment or 
# interest on a home loan

print("Investment - To calculate the amount of interest you'll earn on your investment.")
print("Bond - To calculate the amount you'll have to pay on a home loan.")

# decides which calculator the user has selected

calculator_type = input("\nEnter either 'investment' or 'bond' from the menu above to proceed:").lower()

# if the user enters investment, the details of the investment will be prompted,
# then calucated and displayed
# displays error message if input is invalid

if calculator_type != "investment" and calculator_type != "bond":
    print("Invalid input, please enter 'investment' or 'bond'.")
elif calculator_type == "investment":
    deposit = float(input("Please enter your deposit amount: "))
    interest_rate = float(input("Please enter the interest rate percentage: "))
    investment_years = int(input("Please enter how many years you plan to invest for: "))
    interest = input("Would you like 'simple' or 'compound' interest? ").lower()
    if interest == "simple":
        total_investment = deposit*(1 + ((interest_rate / 100)*investment_years))
        print("Your total investment after depositing " + str(deposit) + " for " + str(investment_years) +
        " years at " + str(interest_rate) + "% interest will be: " + str(total_investment) + ".")
    elif interest == "compound":
        total_investment = deposit * math.pow((1 + (interest_rate / 100)),investment_years)
        print("Your total investment after depositing " + str(deposit) + " for " + str(investment_years) +
        " years at " + str(interest_rate) + "% interest will be: " + str(total_investment) + ".")
    else:
        print("Invalid selection, please select 'simple' or 'compound'.")

# if the user enters bond, the details of the home loan will be prompted, then 
# calculated and displayed

if calculator_type == "bond":
    house_value = int(input("Please enter the house value: "))
    interest_rate_loan = float(input("Please enter the interest rate precentage: "))
    repayment_term = int(input("Please enter the number of months in which you plan \
to repay the loan: "))
    
    monthly_payment = (((interest_rate_loan/100)/12) * house_value)/(1 - (1 + ((interest_rate_loan/100)/12))**(- repayment_term))

    print("Based on the information you have provided, for a house valued at £" +
    str(house_value) + " with an interest rate of " + str(interest_rate_loan) + 
    "% over a term of " + str(repayment_term) + " months, you're monthly repayments \
will be: £" + str(monthly_payment))