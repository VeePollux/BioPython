'''Uma bactéria possui população inicial de 500 indivíduos. Sabe-se que, a cada
intervalo de 3 horas, a população de bactérias aumenta em cerca de 2,5 vezes.
Faça um script que preveja em quantas horas a população de bactérias chegará
a 100.000 indivíduos'''

popinic = 500
min = 0

while(popinic < 100000):
    min +=1
    popinic = popinic * 2.5

print (popinic)
print(min*3)
