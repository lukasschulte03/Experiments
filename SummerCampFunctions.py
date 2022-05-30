import math

def Q0_My_Name_Is():
    # Make this function return your name and email address.
    return "Lukas Schulte, lukas007@live.se"


def Q1_GC_Content(inp):
    # Function content goes here
    # return GC_percent

    GC_count = 0
    for element in inp:
        if element == "G" or element == "C":
            GC_count += 1

    return (GC_count / len(inp)) * 100


def Q2_Translation(inp):
    # Function content goes here
    # return AA_stringz

    dic = {
        "ATA": "I",
        "ATC": "I",
        "ATT": "I",
        "ATG": "M",
        "ACA": "T",
        "ACC": "T",
        "ACG": "T",
        "ACT": "T",
        "AAC": "N",
        "AAT": "N",
        "AAA": "K",
        "AAG": "K",
        "AGC": "S",
        "AGT": "S",
        "AGA": "R",
        "AGG": "R",
        "CTA": "L",
        "CTC": "L",
        "CTG": "L",
        "CTT": "L",
        "CCA": "P",
        "CCC": "P",
        "CCG": "P",
        "CCT": "P",
        "CAC": "H",
        "CAT": "H",
        "CAA": "Q",
        "CAG": "Q",
        "CGA": "R",
        "CGC": "R",
        "CGG": "R",
        "CGT": "R",
        "GTA": "V",
        "GTC": "V",
        "GTG": "V",
        "GTT": "V",
        "GCA": "A",
        "GCC": "A",
        "GCG": "A",
        "GCT": "A",
        "GAC": "D",
        "GAT": "D",
        "GAA": "E",
        "GAG": "E",
        "GGA": "G",
        "GGC": "G",
        "GGG": "G",
        "GGT": "G",
        "TCA": "S",
        "TCC": "S",
        "TCG": "S",
        "TCT": "S",
        "TTC": "F",
        "TTT": "F",
        "TTA": "L",
        "TTG": "L",
        "TAC": "Y",
        "TAT": "Y",
        "TAA": "_",
        "TAG": "_",
        "TGC": "C",
        "TGT": "C",
        "TGA": "_",
        "TGG": "W",
    }

    AA_string = ""
    for i in range(0, len(inp), 3):
        Codon = inp[i] + inp[i + 1] + inp[i + 2]
        AA_string += dic[Codon]

    return AA_string


def Q3_magically_annoying_coin(inp):
    # Function content goes here
    # return log_probability

    K = len(inp)
    prob = 1
    for i in range(0, K):
        if inp[i] == "H":
            prob *= (i + 1) / (K)
        elif inp[i] == "T":
            prob *= 1 - (i + 1) / (K)

    return math.log(prob)


def Q4_Biggest_Product(inp):
    # Function content goes here
    # return start_index,end_index
    indices = (0, 0)
    newVal = 1
    bestVal = 0

    for i in range(0, len(inp)):
        newVal = 1
        for j in range(0, len(inp) - i):
            newVal *= inp[j + i]
            if newVal > bestVal:
                bestVal = newVal
                indices = (i + 1, j + i + 1)

    return indices


def Q5_Data_dumpster_diving():
    # Text only answer. Modify the obviously incorrect answer inside the return statement below.
    # Feel free to add as much explanation as you think you need, but make sure it all gets returned as one string.
    return """The 1722 elements are all atoms. Any coordinate in the symmetric 2D array will give you a value that represents the distance from the atom[x] and the atom[y]. \nI.e. the value at (3,7) will give you the distance between the 3rd and the 7th atoms in the list / one dimensional array. \nThe value at the coordinate (7,3) will return the same value as (3,7), and therefore it is called a "symmetric" 2D array"""


print(" ")
print(Q1_GC_Content("GCATGCACATAGCAGCGAGCTACTACATCGCGGCTAGACTACTGAGCGA"))
print(" ")
print(Q2_Translation("CAGGTGACCTTGAAGGAGTCTGGTCCTGCGCTAGTGAAACCCACACAGACCCTCACGCTGACCTGCACCTTCTCTGGGTTCTCA"))
print(" ")
print(Q3_magically_annoying_coin("HTHHTH"))
print(" ")
print(Q4_Biggest_Product([1.6, 0.56, 1.3, 1.5, 0.9, 1.5, 2.5, 1.1, 0.46, 0.65]))
print(" ")
print(Q5_Data_dumpster_diving())