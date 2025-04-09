def Restriction_enzyme_cut_sites(sequence, restriction_enzyme):
    bases ={"A","T","G","C"} # set bases in DNA
    sites = []
    for i in range(len(sequence)): # check if there are any base not in list
        if sequence[i] not in bases: 
            print("the sequence is wrong")
            return
    enzyme_length = len(restriction_enzyme) # calculate the total length of restriction_enzyme
    for i in range(len(sequence) - enzyme_length + 1): #from 0 to the len(sequence) - enzyme_length + 1
        if sequence[i:i + enzyme_length] == restriction_enzyme: # check if the part of sequence == restriction_enzyme
            sites.append(i+1) # write the place
    if sites == []:
        print("not found")
        return
    else:
      print(sites)
      return sites
Restriction_enzyme_cut_sites("ATCGTTCG","TCG") # find the 2 and 6 is the start of TCG
Restriction_enzyme_cut_sites("ATCGTTCGYS","TCG") # error
Restriction_enzyme_cut_sites("ATCGTTCG","TCGA") # 
