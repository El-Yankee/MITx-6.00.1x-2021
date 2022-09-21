#Credit Card Balance

#Some math tips:
    # Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
    # Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
    # Monthly interest rate = (Annual interest rate) / 12.0    
    # Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
 
#Variables

balance = 484

annualInterestRate = 0.2

monthlyPaymentRate = 0.04

#Code

def bank(balance, annualInterestRate, monthlyPaymentRate):
    """
    Parameters
    ----------
    balance : int or float
        
    anualinter : float/decimal
        
    monthpay : float/decimal
        
    Returns the credit card balance after one year if a person only pays 
    the minimum monthly payment required by the credit card company each month. 
    
    """
    i = 1
    
    while i <= 12:  #12 because its a year
        
        min_month_pay = monthlyPaymentRate * balance    #Minimum monthly payment
    
        mon_unpaid_balance = balance - min_month_pay    #Monthly unpaid balance
    
        balance = mon_unpaid_balance + annualInterestRate/12 * mon_unpaid_balance   #Updated balance each month
        
        i +=1   #Counter for each month
    
    return round(balance, 2)

print ("Remaining balance: " + str(bank(balance, annualInterestRate, monthlyPaymentRate)))