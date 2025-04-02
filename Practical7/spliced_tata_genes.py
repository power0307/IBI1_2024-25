import re

# Get the user input for the splice donor/acceptor combination
splice_combination = input("Please enter one of the splice donor/acceptor combinations (GTAG, GCAG, ATAC): ")
while splice_combination not in ["GTAG", "GCAG", "ATAC"]:
    splice_combination = input("Invalid input. Please enter one of the splice donor/acceptor combinations (GTAG, GCAG, ATAC): ")

# Construct the output file name
output_filename = f"{splice_combination}_spliced_genes.fa"

# Assume gene sequences are read from a file here. For now, simulate the data structure.
# In a real - world application, sequences should be read from an actual fasta file, like the one processed previously.
genes = {
    "gene1": "ATGCTATATATGCTAGCTGTAG",
    "gene2": "ATGCTAGCTAGCTGCAG",
    "gene3": "ATGCTATATAAGCTAGCTATAC"
}

# Compile the regular expression pattern for the TATA box
tata_pattern = re.compile(r"TAT(A{2,6})T")

with open(output_filename, "w") as out_file:
    for gene_name, gene_sequence in genes.items():
        # Check if the gene sequence contains the splice combination
        if splice_combination in gene_sequence:
            # Count the number of TATA boxes in the gene sequence
            tata_count = len(tata_pattern.findall(gene_sequence))
            if tata_count > 0:
                # Remove newline characters from the sequence and write it to the file
                one_line_sequence = gene_sequence.replace("\n", "")
                out_file.write(f">{gene_name}_{tata_count}\n{one_line_sequence}\n")