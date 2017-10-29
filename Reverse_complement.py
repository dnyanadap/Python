import math, string, re

return_value = ""

"""
----------------------------------------------------------------------------------------------------
== FUNCTION 2 ==
Write a function called ReverseComplement, that takes in a sequence as an argument and returns an
output that is the reverse RNA complement of the input. The function reverses the order of the bases 
in the sequence and replaces each base in the reversed sequence with its complement base.  The 
complement base of a gap character is a gap character (e.g. "-" => "-") and irrelevant characters are 
ignored. 
"""

def ReverseComplement(seq):
     """ Function to generate the reverse RNA complement of the given sequence """
     rev_seq = ""
     rev_comp = ""

     seq = seq.replace("T","U")
     for j in seq:
          if j == "A":
               rev_seq += "U"
          elif j == "U":
               rev_seq += "A"
          elif j == "G":
               rev_seq += "C"
          elif j == "C":
               rev_seq += "G"
          elif j == "-":
               rev_seq += "-"
          else:
               pass
          
     for i in range((len(seq)-1),0,-1):
          rev_comp = rev_comp + rev_seq[i]
          
     return rev_comp


#Sample Run:
ReverseComplement("GCAAGC-CGTACG")      #return=>CGUACG-GCUUGC 
