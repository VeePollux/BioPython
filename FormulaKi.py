# -*- coding: utf-8 -*-
print(" FÓRMULA KI ")
IC = int(input("Valor de IC50:"))
S = int(input("Valor de S:"))
Km = int(input("Valor de Km:"))
print(IC / (1 + (S/Km)))
