import math, string, re

return_value = ""

"""
----------------------------------------------------------------------------------------------------
== FUNCTION 1 ==
Write a function called HydrophobicityScore, that takes a protein sequence as its argument.
The function computes the hydrophobicity of the entire sequence based on the following formula:

HydrophobicityScore = 1 / N * [ Sum of hydrophobicity of each amino acid ]
where N = length of the sequence

Below are the hydrophobicity values of the amino acids
     R: -4.5, S: -0.8,
     K: -3.9, T: -0.7,
     N: -3.5, G: -0.4,
     D: -3.5, A: 1.8,
     Q: -3.5, M: 1.9,
     E: -3.5, C: 2.5,
     H: -3.2, F: 2.8,
     P: -1.6, L: 3.8,
     Y: -1.3, V: 4.2,
     W: -0.9, I: 4.5
"""
""" Creating a dictionary for the hydrophobicity values of proteins """
hydro_values = {
      "R": -4.5, "S": -0.8,
     "K": -3.9, "T": -0.7,
     "N": -3.5, "G": -0.4,
     "D": -3.5, "A": 1.8,
     "Q": -3.5, "M": 1.9,
     "E": -3.5, "C": 2.5,
     "H": -3.2, "F": 2.8,
     "P": -1.6, "L": 3.8,
     "Y": -1.3, "V": 4.2,
     "W": -0.9, "I": 4.5}

def HydrophobicityScore(proteinSequence):
     """ Function to calculate the hydrophobicity score of a given protein """
     total = 0.0
     proteinSequence = str.upper(proteinSequence)
     proteinSequence = proteinSequence.strip()
     #print proteinSequence

     for i in range(0,len(proteinSequence)):
          if hydro_values.has_key(proteinSequence[i]):
               score = hydro_values[proteinSequence[i]]
               #print score
               total += score
     #print total
     N = len(proteinSequence)
     hydro_score = 1 * total/N
          
     return hydro_score
