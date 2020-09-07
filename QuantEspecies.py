'''Faça um programa que pergunte ao usuário quantas espécies ele coletou. Em
seguida, o programa deverá perguntar o nome de cada espécie e quantidade coletada,
e armazenar as informações em um dicionário. Posteriormente, ele deve calcular a
soma de todos os indivíduos coletados e a média de ind. coletados por espécie.
Por último, deve imprimir na tela as informações sobre cada espécie nesse formato:

Espécie: xxx, espécimes coletados: xxx
Deve imprimir também a soma e a média de coletas por espécie. '''

coletas = dict()
x = 0
soma = 0
quant = int(input("Quantidade de especies coletadas: "))

while(x < quant):
    nome_esp = str(input("Digite o nome da espécie: "))
    quant_esp = int(input("Digite a quantidade coletada da espécie: "))
    coletas[nome_esp] = quant_esp
    soma = soma + quant_esp
    x +=1

for nome, quantidade in coletas.items():
    print("Espécie:", nome, "Quantidade:", quantidade)
print("Média da quantidade coletada por espécie:", soma/quant, "\nSoma de indivíduos coletados:", soma)
