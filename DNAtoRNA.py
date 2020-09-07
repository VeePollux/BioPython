'''Escreva um programa que tome uma sequência de DNA como input do usuário e
retorne uma sequência de RNA transcrita. CGATTCGTGATCGTATGTCGTGCT'''

DNA = (str(input("Sequência de DNA: "))).upper()

trans = {"A": "U", "T":"A", "C": "G", "G":"C"}
RNA = ""

for nucleotideo in DNA:
    RNA = RNA + trans[nucleotideo]
print("Sequência de RNA:", RNA)
