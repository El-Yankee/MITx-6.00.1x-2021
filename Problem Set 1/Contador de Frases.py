#Contador de frases

s = "bobbobbobbob"
rep = 0

for i in range (len(s)):
    if "bob" in s[i:(i+3)]:
        rep += 1        
    else:
        rep += 0
              
print("Number of times bob occurs is:", rep)