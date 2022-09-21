#Minimum Fixed Monthly Payment

#Some math tips:
    # Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
    # Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
    # Monthly interest rate = (Annual interest rate) / 12.0    
    # Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
 
#Variables----------------------------------------------

balance = 4773

annualInterestRate = 0.2

min_month_pay = 0

result = 1

#Code---------------------------------------------------

def bank(balance, annualInterestRate, min_month_pay):
    """
    Parameters
    ----------
    balance : int or float
        
    annualInterestRate : float/decimal
    
    min_month_pay : int or float
     
    Returns the lowest monthly payment that will pay off all debt in under 1 year 
    
    """
    i = 1
    
    while i <= 12:                                                                  #12 because its a year
        
        mon_unpaid_balance = balance - min_month_pay                                #Monthly unpaid balance
    
        balance = mon_unpaid_balance + annualInterestRate/12 * mon_unpaid_balance   #Updated balance each month
        
        i +=1                                                                       #Counter for each month
    
    return round(balance, 2)


while result > 0:                                                                   #This is for check if we pay all the balance
    
    min_month_pay += 10                                                             #Sum 10 to check if we pay all the balance
    
    result = bank(balance, annualInterestRate, min_month_pay)                       #Balance with new month pay
    
else:
    print("Lowest Payment: " + str(min_month_pay))


#print ("Remaining balance: " + str(result))
