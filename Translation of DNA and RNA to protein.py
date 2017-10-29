
#FUNCTION NAME: RNA2Protein
#PARAMETERS: 1 (An RNA sequence)
#PURPOSE: The function should:
#           (1) Divide the RNA sequence into a list of 3-base codons.
#HINT: You could use CodonList inside this function from previous lecture.
#           (2) Create a new protein string.
#           (3) Use the "standard_code" dictionary to find the amino acid for each codon in the list.
#           (4) Return the new protein string.
#RETURN VALUES: A protein sequence. (A string)

standard_code = {
     "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "UCU": "S",
     "UCC": "S", "UCA": "S", "UCG": "S", "UAU": "Y", "UAC": "Y",
     "UAA": "*", "UAG": "*", "UGA": "*", "UGU": "C", "UGC": "C",
     "UGG": "W", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
     "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P", "CAU": "H",
     "CAC": "H", "CAA": "Q", "CAG": "Q", "CGU": "R", "CGC": "R",
     "CGA": "R", "CGG": "R", "AUU": "I", "AUC": "I", "AUA": "I",
     "AUG": "M", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
     "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "AGU": "S",
     "AGC": "S", "AGA": "R", "AGG": "R", "GUU": "V", "GUC": "V",
     "GUA": "V", "GUG": "V", "GCU": "A", "GCC": "A", "GCA": "A",
     "GCG": "A", "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
     "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

def RNA2Protein(dna):
    prot=""
    for i in range(0,len(dna),3):
        cod = dna[i:i+3]
        #print cod
        if standard_code.has_key(dna[i:i+3]):
            #print standard_code[dna[i:i+3]]
            aa = standard_code[dna[i:i+3]]
            prot = prot + aa
            
    return prot
    
#------------------------------------------------------------------------------------------
#PART 2 -

#FUNCTION NAME: DNA2Protein
#PARAMETERS: 1 (A DNA sequence)
#PURPOSE: The function should:
#           (1) Clean the DNA sequence and convert it to RNA. Just change T's to U's (don't reverse compliment)
#           (2) Divide the RNA sequence into a list of 3-base codons.
#           (3) Create a new protein string.
#           (4) Use the "standard_code" dictionary to find the amino acid for each codon.
#                   [NOTE: Stop translating after "Stop" codons.]
#           (5) Return the new protein string.
#RETURN VALUES: A protein sequence. (A string)


#== FUNCTION 2 ==
def DNA2Protein(fdna):
    fdna = fdna.replace("T","U")
    fdna = fdna.strip()
    rna = str.upper(fdna)
    #print rna

    prot = ""
    codon = []
    for i in range(0,len(rna),3):
        cod = rna[i:i+3]
        codon.append(cod)
        for j in codon:
            try:
                if j in standard_code:
                #print standard_code[rna[i:i+3]
                    amino_acid = standard_code[rna[i:i+3]]
                    prot += amino_acid
                if amino_acid == "*":
                    break
                    
            except:
                prot += "?"
    return prot 
    

#------------------------------------------------------------------------------------------

#== FUNCTION 3 ==

#FUNCTION NAME: EC_TranslateSeq
#PARAMETERS: 2 (A sequence, and a default integer parameter set equal to "0")  
#PURPOSE: The function should:
#           (1) Clean the sequence.
#           (2) Check to see if the sequence is RNA or DNA. If it is DNA, convert it to RNA.
#           (3) Divide the RNA sequence into a list of 3-base codons.
#           (4) Create a new protein string.
#           (5) Based on the second parameter, use the appropriate dictionary 
#                   (if 0 use "standard_code", else use "mitochondrial_code")

#           (6) Return the new protein string.

#RETURN VALUES: A protein sequence. (A string)


mitochondrial_code = {
     "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "UCU": "S",
     "UCC": "S", "UCA": "S", "UCG": "S", "UAU": "Y", "UAC": "Y",
     "UAA": "*", "UAG": "*", "UGU": "C", "UGC": "C", "UGA": "W",
     "UGG": "W", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
     "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P", "CAU": "H",
     "CAC": "H", "CAA": "Q", "CAG": "Q", "CGU": "R", "CGC": "R",
     "CGA": "R", "CGG": "R", "AUU": "I", "AUC": "I", "AUA": "M",
     "AUG": "M", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
     "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "AGU": "S",
     "AGC": "S", "AGA": "*", "AGG": "*", "GUU": "V", "GUC": "V",
     "GUA": "V", "GUG": "V", "GCU": "A", "GCC": "A", "GCA": "A",
     "GCG": "A", "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
     "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}


#== FUNCTION 3 ==
def EC_TranslateSeq(fseq, fcode=0):                    
        
    fseq = fseq.strip()
    fseq = str.upper(fseq)
    for nuc in fseq:
        if nuc == "T":
            fseq = fseq.replace("T","U")
        else:
            pass
    print fseq

    prot=""
    for j in range(0,len(fseq),3):
        cod = fseq[j:j+3]
        print cod
        if fcode == 0:
            if standard_code.has_key(fseq[j:j+3]):
                
                amino_acid = standard_code[fseq[j:j+3]]
                prot = prot + amino_acid
                if amino_acid == "*":
                    break
                else:
                    pass
        elif fcode == 1:
            if mitochondrial_code.has_key(fseq[j:j+3]):
                
                a_a = mitochondrial_code[fseq[j:j+3]]
                prot = prot + a_a
                if a_a == "*":
                    break
                else:
                    pass
        elif fcode == "":
            if standard_code.has_key(fseq[j:j+3]):
                
                amino_acid = standard_code[fseq[j:j+3]]
                prot = prot + amino_acid
                if amino_acid == "*":
                    break
                else:
                    pass     
            
    return prot  
    


rna1=" \n \tAUGcaaGCAGuuACAUGAGagguAGGCAAGCACGCAGGAAC   \n\t"
dna1=" \n atGTTCAtagTCATTATagTTacagTATTATtCTGa \n\t"

#Test the function with the following sequences using both "standard" and "mitochondrial" codes:
rna1=" \n \tAUGcaaGCAGuuACAUGAGagguAGGCAAGCACGCAGGAAC   \n\t"
dna1=" \n atGTTCAtagTCATTATagTTacagTATTATtCTGa \n\t"

#" \n \tAUGcaaGCAGuuACAUGAGagguAGGCAAGCACGCAGGAAC   \n\t"
#"\n  AUGccaaGAGActGAgCC \t\n"
                
