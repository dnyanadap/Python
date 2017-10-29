import math, string, re

return_value = ""

"""
----------------------------------------------------------------------------------------------------
== FUNCTION 4 ==
Write a function called MotifMatch, that takes a sequence as an argument. The function returns
the string "Match" or "Not Match" depending on whether or not the given sequence matches the
following motif:

          [WP]- x - [CDV] - M - [HYM] - x - [IM] - [DCT] - [HWN] - S

Be sure to clean your sequence of any invalid characters.
"""

def MotifMatch(seq):

     """ Function to match a motif in a given sequence """
     y = re.search("[WP][A-Z][CDV]M[HYM][A-Z][IM][DCT][HWN]S",seq)

     if y:
          ans = "Match"
          return ans
     else:
          ans2 = "Not Match"
          return ans2

     
     return return_value
        
#Sample Run:
MotifMatch("WWDMHXIDHS")      #return => Match 
MotifMatch("P-VCYwMTWS")      #return => Not Match 
