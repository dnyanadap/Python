#FUNCTION NAME: CodonList
#PARAMETERS: 1 (A sequence)
#PURPOSE: The function should:
#           (1) Iterate through the sequence.
#           (2) Divide the sequence into sections of 3-base codons with NO OVERLAPPING.
#           (3) Add the codons to a list.
#                   [NOTE: If a group is not 3 bases long, do not include it in the list.]
#           (4) Return the list.
#RETURN VALUES: A list of codons. (A list)

#== FUNCTION 1 ==
def CodonList(rna):
    codons=[]
    i=0
    for i in range(0,len(rna)-2,3):
        print i
        codon=rna[i:i+3]
        if len(codon)==3:
            codons.append(codon)
        else:
            pass
    return codons

#EXAMPLE:
#dna1="AUGGGAAGCTTT"
