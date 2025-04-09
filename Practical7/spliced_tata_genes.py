import re

file_path = r"C:\Users\F\Desktop\IBI1\IBI1_2024-25\Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
tata_patterns = ["GTAG", "GCAG", "ATAC"]  # give the pattern
a = input("Choose GTAG or GCAG or ATAC: ").strip().upper() 
if a not in tata_patterns:
    print("Invalid choice. Please enter GTAG, GCAG, or ATAC.")
    exit()
output_path = rf"C:\Users\F\Desktop\IBI1\IBI1_2024-25\Practical7\{a}_spliced_genes.fa"
with open(file_path, "r") as file, open(output_path, "w") as newfile:
    current_header = ""
    current_sequence = []
    
    for line in file:  # check line in the file one by one
        if line.startswith(">"):  # find the ">" in the line
            if current_header and current_sequence:  # check if these two things are full
                full_sequence = "".join(current_sequence)
                count = len(re.findall(a, full_sequence))
                if count > 0:
                    newfile.write(f"{current_header[:8]}\n")
                    newfile.write(f"Number of {a} : {count}\n")
                    newfile.write(f"{full_sequence}\n\n")
            
            current_header = line.strip()
            current_sequence = []
        else:
            current_sequence.append(line.strip())
    
    # Handle the last gene
    if current_header and current_sequence:
        full_sequence = "".join(current_sequence)
        count = len(re.findall(a, full_sequence))
        if count > 0:
            newfile.write(f"{current_header[:8]}\n")
            newfile.write(f"Number of {a} : {count}\n")
            newfile.write(f"{full_sequence}\n\n")