import sys

def parse_gff(gff_file):
    """
    Function to parse GFF file and print the length of each feature.
    """
    with open(gff_file, 'r') as file:
        for line in file:
            # Strip line breaks and split by tab character
            data = line.strip().split('\t')
            # Check if the line is not a comment
            if not line.startswith('#'):
                # Print the length of the feature
                print("Length of feature:", abs(int(data[4]) - int(data[3])))

def main():
    """
    Main function to parse command-line arguments and execute parsing of GFF file.
    """
    # Check if correct number of arguments provided
    if len(sys.argv) != 3:
        print("Usage: python parseGFF.py <GFF file> <FASTA file>")
        sys.exit(1)

    gff_file = sys.argv[1]
    fasta_file = sys.argv[2]

    # Parse GFF file
    parse_gff(gff_file)

if __name__ == "__main__":
    main()
