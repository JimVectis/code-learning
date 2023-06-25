import math

print("investment \t - to calculate the amount of interest you'll earn on your investment")
print("bond \t\t - to calculate the amount you'll have to pay on a home loan")

user_action = input("Please enter either 'investment' or 'bond' from the menu above to proceed: ")

if  user_action.lower() == "investment":
    deposit = int(input("Please state the amount of money you are despositing: "))
    rate = int (input("Please state the interest rate as a percentage: "))
    years = int(input("Please state the number of years you plan to invest for: ")) 
    interest_type = (input("Please select the type of interest you would like by stating 'simple' or 'compound': "))
    interest = interest_type.lower()

    if interest == "simple":
    #This section will calculate simple interest
        amount = deposit*(1+(rate/100)*years)
        print("After", years, "years, you will have", amount)
        
    elif interest == "compound":
    #This section will calculate compound interest
        amount = deposit*math.pow((1+(rate/100)),years)
        print("After", years, "years, you will have", amount)
    
    else:
         print ("Please check you have entered 'simple' or 'compound' correctly")

elif user_action.lower() == "bond":
    P = int(input("Please state the present value of the house: "))
    interest = int(input("Please state the interest rate as a percentage: "))
    i = (interest/100)/12       # Converts annual interest to monthly
    n = int(input("Please state the number of months you plan to take to repay the bond: "))

    # this will calculate the montly repayment
    repayment = (i*P)/(1 - (1+i)**(-n))
    print("For a bond of", n, "months, you will have to repay", repayment, "per month.")

else:
        print("Please check you have entered 'investment' or 'bond' correctly")