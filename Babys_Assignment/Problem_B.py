'''
Purpose : Identify the complement of a dna strand 
Parameters : dna string type 
Return Values : complement string type
'''
def dna_complement (dna):
    
    #Normalize the String
    dna.upper()
    complement_strand = ''
    
    for nt_base in dna:
        if nt_base == 'G':
            complement_strand = complement_strand + 'C'
        elif nt_base == 'C':
            complement_strand = complement_strand + 'G'
        elif nt_base == 'A':
            complement_strand = complement_strand + 'T'
        elif nt_base == 'T':
            complement_strand = complement_strand + 'A'
    return complement_strand

def problem_b_Fomating():
    print("_______Dna Complements__________")


if __name__ == '__main__':
    problem_b_Fomating()
    print(dna_complement("GCC"))
    print(dna_complement("AGCTTTCATTCTGA"))
    print(dna_complement("CCGTACGC"))