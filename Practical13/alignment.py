human = r"C:\Users\F\Desktop\IBI1\IBI1_2024-25\Practical13\uniprotkb_accession_P04179_2025_05_13.fasta"
mouse = r"C:\Users\F\Desktop\IBI1\IBI1_2024-25\Practical13\mouse.fasta"
random = r"C:\Users\F\Desktop\IBI1\IBI1_2024-25\Practical13\random.fasta"

def read_sequence(filename):
    sequence = []
    # Open the file in read - only mode. The 'with' statement ensures the file is properly closed after use.
    with open(filename, 'r') as f:
        # Iterate over each line in the file
        for line in f:
            line = line.rstrip()
            # Skip lines that start with '>', which are often comment lines in sequence files
            if not line.startswith('>'):
                sequence.append(line)
    # Concatenate the elements in the sequence list into a single string and return it
    return ''.join(sequence)

# Read the human, mouse, and random sequences respectively
human_sequence = read_sequence(human)
mouse_sequence = read_sequence(mouse)
random_sequence = read_sequence(random)

matrix = []
with open (r"C:\Users\F\Desktop\IBI1\IBI1_2024-25\Practical13\BLOSUM62.txt", "r") as m:
    for line in m:
        if not line.startswith('#'):
            matrix.append(line)

def calculate_edit_distance(seq1, seq2):
    match = []
    for i in range(len(seq1)):
        match.append(seq1[i]+seq2[i])
    edit_distance = 0  # Initialize the edit distance to 0
    # Iterate over the indices of seq1
    for i in range(len(seq1)):
        # If the amino acids at the current index in seq1 and seq2 are different
        if seq1[i] == seq2[i]:
            edit_distance += 1  # Increment the edit distance by 1
    percentage = float(edit_distance / len(seq1)) * 100  # Calculate the percentage of different amino acids

    score = 0
    for i in match:
        for x in range(len(matrix[0])):
            for y in range(len(matrix)):
                if matrix[0][x] == i[0] and matrix[y][0] == i[1]:
                    score += int(matrix[y][x])
    print(score)
    print("The percentage of indentical amino acids: ", "%.2f" % percentage, "%")  # Print the percentage of identical amino acids with 2 decimal places
    return edit_distance  # Return the edit distance

# Compare the human and mouse sequences for the same - length parts
print("human and mouse")
calculate_edit_distance(human_sequence, mouse_sequence)
# Compare the human and random sequences for the same - length parts
print("human and random")
calculate_edit_distance(human_sequence, random_sequence)
# Compare the mouse and random sequences for the same - length parts
print("random and mouse")
calculate_edit_distance(mouse_sequence, random_sequence)

# The length and subcellular localisation of the human SOD2	protein: 
# length: 222
# localisation: mitochondrion matrix
# humans and random are most closely