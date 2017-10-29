import math, string, re

return_value = ""

"""
----------------------------------------------------------------------------------------------------
== FUNCTION 3 ==
Write a function called FindStart, that takes in a sequence and a filename as its arguments. 
If the function locates the starting position of the first start codon ("AUG") within the sequence
then it writes the rest of the RNA bases and/or gaps in the sequence into the file named in the argument.  
If a start codon is not found in the sequence the function returns "None" otherwise the starting 
position of the first start codon should be returned.
"""

def FindStart(seq,outfile):
     """ Function to find the start codon and return its position in a given sequence """
     fout = open(outfile,'w')
     prot = ""
     cod = []

     for i in range(0,len(seq)):
          codon = seq[i:i+3]
          cod.append(codon)
    
     for k in range(0,len(cod)):
          if cod[k] == "AUG":
               start_pos = cod.index(cod[k])
               for j in range(k+3,len(seq)):
                    prot = prot + seq[j]
               fout.write(prot)
               fout.close()
          
     if "AUG" in cod:
          return start_pos
     else:
          val = "None"
          return val
      
     return return_value
#Sample Run:
FindStart("GCAUGCCGUACG","output.txt")                 #return => 2
#Contents of output.txt =>CCGUACG
		
FindStart("CG----UACGGCA---UGC","output.txt")          #return => None
