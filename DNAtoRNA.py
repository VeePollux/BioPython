'''Escreva um programa que tome uma sequência de DNA como input do usuário e
retorne uma sequência de RNA transcrita. CGATTCGTGATCGTATGTCGTGCT'''

DNA = (str(input("Sequência de DNA: "))).upper()

RNA = ""

for nucleotideo in DNA:
    if nucleotideo == "A":
        RNA = RNA + "U"
    elif nucleotideo == "T":
        RNA = RNA + "A"
    elif nucleotideo == "C":
        RNA = RNA + "G"
    elif nucleotideo == "G":
        RNA = RNA + "C"
print("Sequência de RNA:", RNA)
