#---------------------------------------------------------------------------------
#FUNCTION NAME: NmerList 
#PARAMETERS: 2  (A sequence, and an integer for the length of the nmers)
#PURPOSE: The function should:
#           (1) Clean the sequence.
#           (2) Iterate through the sequence.
#           (3) Divide the sequence into sections of a given length (nmers) with NO OVERLAPPING.
#           (4) Add the nmers to a list.
#           (5) Return the list.
#RETURN VALUES: A list of nmers. (A list)
#
#== FUNCTION 2 ==
def NmerList(fseq,num):
 return

def NmerList(fseq,num):
    fseq = str.upper(fseq)
    fseq = fseq.strip()
    fseq = fseq.replace(" ","")
    print fseq
    nmer_list=[]

    for i in range(0,len(fseq)-(num-1),num):
        nmers = fseq[i:i+num]
        nmer_list.append(nmers)
    return nmer_list


#dna2="AaUGGcGAAgcG \n"
#nmer_list=NmerList(dna2, 4)
#print nmer_list
