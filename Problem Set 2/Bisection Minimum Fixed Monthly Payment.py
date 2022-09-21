#Bisection Minimum Fixed Monthly Payment

#Some math tips:
    # Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
    # Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
    # Monthly interest rate = (Annual interest rate) / 12.0    
    # Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
    # Monthly payment lower bound = Balance / 12
    # Monthly payment upper bound = (Balance x (1 + Monthly interest rate)**12) / 12.0
 
#Variables----------------------------------------------

balance = 999999

annualInterestRate = 0.18

month_pay_low = balance/12

month_pay_upp = (balance * ((1 + (annualInterestRate/12))**12))/12

guess = 0

result = 1

#Code---------------------------------------------------

def bank(balance, annualInterestRate, guess):
    """
    Parameters
    ----------
    balance : int or float
        
    annualInterestRate : float/decimal
    
    guess : int or float
     
    Returns the lowest monthly payment that will pay off all debt in under 1 year
    
    """
    i = 1
    
    while i <= 12:                                                                      #12 because its a year
        
        mon_unpaid_balance = balance - guess                                            #Monthly unpaid balance
    
        balance = mon_unpaid_balance + annualInterestRate/12 * mon_unpaid_balance       #Updated balance each month
        
        i +=1                                                                           #Counter for each month
    
    return round(balance, 2)


while result != 0 :
    
    guess = (month_pay_low + month_pay_upp)/2                                           #Guess using bisection
    
    result = bank(balance, annualInterestRate, guess)                                   #Test using new guess
    
    if result > 0:                                                                      #If result (+) then use a higher guess
        
        month_pay_low = guess
        
    else:                                                                               #If result (-) then use a lower guess
        
        month_pay_upp = guess
    

print("Lowest Payment: " + str(round(guess, 2)))

print ("Remaining balance: " + str(result))
