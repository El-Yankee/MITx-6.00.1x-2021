#Orden Alfabetico

s = "azcbobobegghakl"

frase1 = s[0]
frase2 = frase1

for i in range (1, len(s)):
    if s[i] >= frase2 [-1]:
        frase2 += s[i]
        if len(frase2) > len(frase1):
            frase1 = frase2
    else:
        frase2 = s[i]

print("Longest substring in alphabetical order is: " + frase1)
        