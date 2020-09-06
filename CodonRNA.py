'''Escreva um programa em que o usuário deve digitar uma sequência de RNA. O programa
deve retornar se há um códon de iniciação (AUG), se há um códon de terminação
(UGA, UAA, UAG) ou se há os dois ou nenhum. AGUCAGUCGCUGCAGUCUGCAGCCGACCGCUGCCCC'''

RNA = str(input("Escreva a sequência de RNA:"))

if("AUG" in RNA):
    if("UGA" or "UAA" or "UAG") in RNA:
        print("Possui códon de iniciação e terminação")
    else:
        print("Possui apenas códon de iniciação")
elif("UGA" or "UAA" or "UAG") in RNA:
    print("Possui apenas códon de terminação")
else:
    print("Não possui códon de iniciação ou terminação")
