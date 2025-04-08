def Restriction_enzyme_cut_sites(sequence, restriction_enzyme):
    list ={"A","T","G","C"} # set bases in DNA
    index = 0
    sites = []
    for i in range(len(sequence)): # check if there are any base not in list
        if sequence[i] not in list:
            print("the sequence is wrong")
            return
    while True:
        index = sequence.find(restriction_enzyme,index) # find the location
        if index == -1: # the situation that the all restriction_enzyme are found
          break
        sites.append(index)
        index += 1 # continue the method
    print(sites)
    return sites
Restriction_enzyme_cut_sites("ATCGTTCG","TC")