'''O usuário deve digitar o nome de uma família biológica. Se o nome da família
terminar com -aceae, o programa deve informar que se trata de uma família de
plantas; se terminar com -idae, se trata de uma família de animais; se não tiver
nenhum sufixo, o programa deve afirmar que se trata de um táxon desconhecido'''

nome = str(input("Digite o nome de uma família biológica:"))
if (nome.find("idae")>=0):
    print("Família de animais")
elif(nome.find("aceae")>= 0):
    print("Família de plantas")
else:
    print("Não foi posível identificar a família taxonômica")

#OU
nome = str(input("Digite o nome de uma família biológica:"))
if nome[-4:] == "idae":
  print("Família de animais")
elif nome[-5:] == "aceae":
  print("Família de plantas")
else:
  print("Não foi posível identificar a família taxonômica")
