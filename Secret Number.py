#Secret Number

#Variables:
    
confirmation = ""
guess = 0
low = 0
high = 100

#Code:
    
print("Please think of a number between 0 and 100!")
    
while confirmation != "c":
            
    guess = int((low+high)/2)
    
    print ("Is your secret number " + str(guess) + "?")
    
    confirmation = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    
    if confirmation != "h" and confirmation != "l" and confirmation != "c":
        
        print("Sorry, I did not understand your input.")
        
    else:
        
        if confirmation == "h":
            
            high = guess
        
        elif confirmation == "l":
            
            low = guess
            
        else:
            
            print("Game over. Your secret number was: " + str(guess))