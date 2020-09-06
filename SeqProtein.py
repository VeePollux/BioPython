'''Abaixo há a representação de duas proteínas.
Uma delas é mutante pois teve uma de suas metioninas mutadas para 'leucina' e,
portanto, é maior que sua versão normal. Com base nas sequências, calcule:
a) Quanto (%) a proteína mutante é maior que a normal
b) O comprimento de aa's de cada proteína
c) A porcentagem de serina (S) nas duas sequências'''

proteina1 = 'MGTACHMCGYGCYGYGSHSCIOOENNFHEF'
proteina2 = 'MCCFOTYOOANLGTACHMCGYGCYGYGSHSCIOOENNFHEF'

razao = (len(proteina2)/len(proteina1)-1)*100
print(round(razao,2))

print('O comprimento da proteína 1 é de ',len(proteina1),'aas')
print('O comprimento da proteína 2 é de ',len(proteina2),'aas')

porcentS1 = (proteina1.count("S"))/len(proteina1)*100
porcentS2 = (proteina2.count("S"))/len(proteina2)*100
print("Porcentagem de Serina na proteina 1:", round(porcentS1,2))
print("Porcentagem de Serina na proteina 2:", round(porcentS2,2))
