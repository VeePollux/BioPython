'''O usuário deve digitar um nome científico de uma espécie. O programa deve
deixar a inicial do nome em maiúscula. Em seguida, o programa deverá abreviar o
nome científico, deixando apenas a inicial do gênero e o epíteto específico'''

nome = str(input("Nome:"))
cap = (nome.strip()).capitalize()
abrev = cap[0] + "." + cap[cap.find(" "):]
print("Nome capitalizado: ", cap,"\n", "Nome abreviado:", abrev)
