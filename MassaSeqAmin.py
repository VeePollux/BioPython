'''O usuário deve digitar uma sequência de aminoácidos. O programa deverá validar
se essa sequência é válida (se a string contém letras de aminoácidos) e depois
deve retornar a massa dessa sequência de acordo com a massa de cada aa em um dicionário.
arndedarnhy'''

massa_seq = 0

massa={'A':71.08,
    'R':156.19,
    'N':114.11,
    'D':115.09,
    'C':103.15,
    'E':129.12,
    'Q':128.13,
    'G':57.05,
    'H':137.14,
    'I':113.16,
    'L':113.16,
    'K':128.18,
    'M':131.20,
    'F':147.18,
    'P':97.12,
    'S':87.08,
    'T':101.11,
    'W':186.22,
    'Y':163.18,
    'V':99.13}


while True:
    seq = str(input("Sequência de aminoácidos:")).upper()
    invalida = False
    for aa in seq:
        if aa not in massa.keys():
            invalida = True
    if invalida == False:
        break
    else:
        print('Sequência inválida')

for aa in seq:
    massa_seq = massa_seq + massa[aa]

print("A massa correspondente da sequência digitada é de:",round(massa_seq,2),"g/mol")
