'''
Purpose : Calcualte the GC content of a dna String 
Parameters : dna string type 
Return Values : GC_percentage float type     
'''
def gc_content (dna):
    #Normalize the string 
    dna.upper()

    #Warden 
    if len(dna) == 0:
        return 0.0

    strand_len = len(dna)

    # GC_count
    GC_count = 0

    # forLoop : Checks for G and C, updates GC_count +1 
    for nt_base in dna:
        if nt_base == 'G' or nt_base == 'C':
            GC_count += 1
        
    GC_percentage = GC_count / strand_len

    return GC_percentage

if __name__ == '__main__':
    print(gc_content("GCC"))
    print(gc_content("AGCTTTCATTCTGA"))
    print(gc_content("CCGTACGC"))
