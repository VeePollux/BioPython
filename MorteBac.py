'''Uma bactéria, que possui população inicial de 500 indivíduos, possui o
seguinte padrão de crescimento:
1- Uma fase lag, onde não há crescimento bacteriano (dura 15h)
2- Uma fase exponencial, onde a população aumenta 2,5x a cada hora (dura 10h)
3- Uma fase estacionária, onde a população não cresce (dura 5h)
4 - Uma fase de morte, onde a cada hora, 50% da população bacteriana morre (número de horas desconhecido)
Faça um programa que, com base na população inicial, e padrão de crescimento em
cada fase, descubra em quantas horas a população de bactérias será reduzida a zero'''
horas = 0
pop = 500

while (pop > 0):
    if(horas <= 15):
        pop = pop
    elif(horas <= 25):
        pop = pop*2.5
    elif(horas <= 30):
        pop = pop
    else:
        pop = int(pop*0.5)
    horas +=1
    print("Numero de bacterias em", horas,"horas: ", pop)

print("Total de horas para que toda população bacteriana morra:", horas)
