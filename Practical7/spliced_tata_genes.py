import re
import sys
import os

os.chdir(r"C:\Users\F\Desktop\IBI1\IBI1_2024-25\Practical7")

def main():
   # Define allowable splicing donor/acceptor combinations
    valid_combos = {"GTAG", "GCAG", "ATAC"}

    # Prompts the user for input and converts to uppercase, removing white space
    combo = input("Please enter a splicing donor/acceptor combination（GTAG、GCAG、ATAC）：").strip().upper()
    if combo not in valid_combos:
        sys.exit("Input error, please enter GTAG、GCAG or ATAC")

    # Construct output file name
    output_filename = f"{combo}_spliced_genes.fa"
    # Suppose the input file is named output.fasta (the header line in this file contains only the gene name)
    input_filename = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"

    # Define regular expressions for TATA boxes (W can be either A or T)
    tata_pattern = re.compile(r'TATA[AT]A[AT]', re.IGNORECASE)

    with open(input_filename, 'r') as fin, open(output_filename, 'w') as fout:
        gene_name = None
        seq_lines = []
        for line in fin:
            line = line.rstrip()
            if line.startswith('>'):
                # If it is not the first record in the file, the previous record is processed
                if gene_name is not None:
                    full_seq = "".join(seq_lines)
                    # Count the number of TATA box instances
                    matches = tata_pattern.findall(full_seq)
                    tata_count = len(matches)
                    # Added splice combination check: Output only if the sequence contains both a user-specified splice combination and a TATA box
                    if tata_count > 0 and combo in full_seq:
                        # The header line contains only the gene name and the number of TATA box instances, underlined
                        fout.write(">" + gene_name + "_" + str(tata_count) + "\n")
                        # Output the concatenated sequence of the entire row
                        fout.write(full_seq + "\n")
                # Process new records assuming only the gene name is included in the header row (remove '>')
                gene_name = line[1:].split()[0]
                seq_lines = []
            else:
                # Cumulative sequence row
                seq_lines.append(line)
        # Process the last record at the end of the file
        if gene_name is not None:
            full_seq = "".join(seq_lines)
            matches = tata_pattern.findall(full_seq)
            tata_count = len(matches)
            if tata_count > 0 and combo in full_seq:
                fout.write(">" + gene_name + "_" + str(tata_count) + "\n")
                fout.write(full_seq + "\n")

    print(f"Results have been saved to {output_filename}")


if __name__ == '__main__':
    main()
