'''Faça um programa que pergunte a um individuo do sexo masculino três parâmetros
hematológicos, sendo estes: hemácias, hemoglobina e hematócrito. Cada parâmetro
terá um status (normal ou alterado). Para estar normal, hemácias deve estar entre
4,5 e 5,5; para hemoglobina, deve estar entre 13 e 17; para o hematócrito, deve
estar entre 40 e 50. Caso contrário, o status é considerado alterado. No final,
o programa deve imprimir uma frase para cada status, dizendo se está normal ou alterado.'''

hemac = float(input("Hemácias (x10^12/L):"))
hemog = float(input("Hemoglobina (g/dL):"))
hemat = float(input("Hematócrito (%):"))

if ((hemac > 5.5) or (hemac < 4.5)):
    print("Nível de hemácias: Alterado")
else:
    print("Nível de hemácias: Normal")

if ((hemog> 17) or (hemog < 13)):
    print("Nível de hemoglobina: Alterado")
else:
    print("Nível de hemoglobina: Normal")

if ((hemat> 50) or (hemat < 40)):
    print("Nível de hematócrito: Alterado")
else:
    print("Nível de hematócrito: Normal")
