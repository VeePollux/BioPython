EspA = int(input("Espécies na seção A:"))
IndA = int(input("Indivíduos na seção A:"))
EspB = int(input("Especies na seção B:"))
IndB = int(input("Indivíduos na seção B:"))

ResultA = IndA/EspA
ResultB = IndB/EspB

if(IndA >= IndB):
    print("Quantidade de indivíduos na seção A é maior ou igual a seção B")
    if((IndA > IndB) | (ResultA > ResultB)):
        print("Indivíduos da seção A ou média A é maior que B")
if(IndA != IndB):
    print("Números de indivíduos da seção A e B são diferentes")
    if(ResultA != ResultB):
        print("Média da seção A e B são diferentes")
