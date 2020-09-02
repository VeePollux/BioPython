genrec1 = int(input("Quantidade de gametas recombinantes 1:"))
genrec2 = int(input("Quantidade de gametas recombinantes 2:"))
gennaorec1 = int(input("Quantidade de gametas não recombinantes 1:"))
gennaorec2 = int(input("Quantidade de gametas não recombinantes 2:"))
FR = (genrec1 + genrec2) / (genrec1 + genrec2 + gennaorec1 + gennaorec2)

print("A distância estimada entre os genes é de " + '{0:.3f}'.format(FR*100))
