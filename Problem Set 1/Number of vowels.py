#Number of vowels

s = "aaaaaaaa"
voc = 0

for i in range (len(s)):
    if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u":
        voc += 1
    else:
        voc += 0
        
print ("Number of vowels:", voc)
