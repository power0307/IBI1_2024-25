import re

file_path = r"C:\Users\F\Desktop\IBI1\IBI1_2024-25\Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
#give the pattern
tata_patterns = ["TATATAT", "TATAAAT", "TATAAAA", "TATATAA"]

with open(file_path, "r") as file, open(r"C:\Users\F\Desktop\IBI1\IBI1_2024-25\Practical7\data_genes.fa","w") as newfile: #open the file and read them
    current_header = ""
    current_sequence = []
    
    for line in file: # check line in the file one by one
        if line.startswith(">"): # find the ">" in the line
            if current_header and current_sequence:  # check if these two things are full
                full_sequence = "".join(current_sequence) 
                for pattern in tata_patterns: # check if the sequence meet the patterns
                    if pattern in full_sequence:
                        newfile.write(f"{current_header[:8]}\n")
                        newfile.write(f"{full_sequence}\n")
                        break  #break if a pattern is found
            
            # get the gene name without its sequences
            current_header = line.strip()
            current_sequence = []
        else:
            current_sequence.append(line.strip() + '\n')
    
    # deal with the last gene
    if current_header and current_sequence:
        full_sequence = "".join(current_sequence)
        for pattern in tata_patterns:
            if pattern in full_sequence:
                newfile.write(f"{current_header[:8]}\n")
                newfile.write(f"{full_sequence}\n")
                break  