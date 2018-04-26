interestrate = eval(input("Enter your  interest rate: "))
years = eval(input("Enter your loan years: "))
amount = eval(input("Enter your loan amount: "))
total = (interestrate + 1) ** years * amount
monthly = (amount * interestrate / 12) / (1 - 1/(1 + interestrate / 12) **(12 * years))
print("your total payment is " + str(total) + " and your monthlypayment is " + str(monthly))
