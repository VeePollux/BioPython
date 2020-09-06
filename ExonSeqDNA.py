'''A sequência abaixo representa um pré-mRNA, ou seja, um RNA não processado,
no qual os íntrons não foram removidos. Essa sequência possui um éxon, que
começa com AUG e termina com um stop códon UAG. Determine em que posições
começam os códons de iniciação e parada e retorne o éxon dessa sequência '''

seqRNA='AAAUUUAUGUUCCCUUUGGGUGGGCCCGGGAAAUAGUUCUUGUUUAAAUUC'

exon = seqRNA[seqRNA.find("AUG"):seqRNA.find("UAG")]
exon_codon_parada = seqRNA[seqRNA.find("AUG"):seqRNA.find("UAG")+3]
print("A região codificadora é:", exon)
print("A região codificadora com codon de iniciação e parada é:\n", exon_codon_parada)
