""""

Create a function that finds the reverse complement of a ribonucleic acid (RNA) strand. The RNA will be represented as a string containing only the characters "A", "C", "G" and "U". Since RNA can only (canonically) allow pairings of A/U and G/C, the complement of an RNA would be as follows:
original -> complement
"AAA" -> "UUU"
"UUU" -> "AAA"
"GGG" -> "CCC"
"CCC" -> "GGG"
"GGAACC" -> "CCAAGG"
Your function should find the complement on the right AND also reverse the resulting string.
Examples
reverse_complement("GUGU") ➞ "ACAC"
reverse_complement("UCUCG") ➞ "CGAGA"
reverse_complement("CAGGUAGC") ➞ "ACCUG"
""""



def reverse_complement(input_sequence):
   rna_dict = {"A": "U", "G": "C", "U": "A", "C": "G"}
   return "".join([i.replace(i, rna_dict[i]) for i in input_sequence])[::-1]