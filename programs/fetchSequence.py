from Bio import Entrez, SeqIO

# Set your email here; it's required by NCBI Entrez
Entrez.email = "sarthak.enigma@gmail.com"

# List of accession codes with their corresponding species type (as tuples)
accession_codes = [
    ("NC_020035", "Cat"),
    ("NC_002008", "Dog"),
    # ("NM_007294", "Human (BRCA1)")
    ("NM_001301564", "Zebrafish (Fibronectin)"),
    ("NM_001301717", "Mouse (Apolipoprotein E)"),
    ("NM_001301179", "Chicken (Insulin)"),
    # ("NC_037538","Blue Whale")
    ("NC_004388","Chimpanzee"),
    ("NC_047460","Eagle"),
    ("NC_031598","Butterfly"),
    ("NC_042066","Dolphin")

]

# Set the maximum length for the sequence to print
max_length = 1000  # Adjust this as needed

def fetch_sequences(accession_list):
    for accession, species in accession_list:
        try:
            # Fetch the sequence
            handle = Entrez.efetch(db="nucleotide", id=accession, rettype="fasta", retmode="text")
            # Read the sequence data
            seq_record = SeqIO.read(handle, "fasta")
            handle.close()
            
            # Limit the sequence length if necessary
            sequence = str(seq_record.seq)[:max_length]  # Get only the first max_length characters

            # Print the accession, species, and sequence
            print(f"Species: {species}")
            print(f"Accession: {seq_record.id}")
            print(f"Sequence:\n{sequence}\n")
        except Exception as e:
            print(f"Could not retrieve {accession}: {e}")

# Call the function to fetch and print sequences
fetch_sequences(accession_codes)
