import re 
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
matches = list(re.finditer(r'GT.*?AG', seq)) #match the appropriate consequences
if matches:
    max_length = max(len(match.group()) for match in matches) #find the max length in the match outcomes
    print(f"{max_length}")
    for match in matches:  #find the corresponding consequence that has max length
        if len(match.group()) == max_length:
            print(f"the longest sequence: {match.group()}") #print the corresponding consequence