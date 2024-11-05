import mysql.connector
from Bio.Align import PairwiseAligner
from Bio import Entrez, SeqIO

# Set your email here; it's required by NCBI Entrez
Entrez.email = "sarthak.enigma@gmail.com"

# List of accession codes with their corresponding species type
accession_codes = [("NC_020035", "Cat"), ("NC_002008", "Dog ")]

# Function to fetch sequences from NCBI
def fetch_sequences(accession_list):
    sequences = {}
    
    for accession, species in accession_list:
        try:
            handle = Entrez.efetch(db="nucleotide", id=accession, rettype="fasta", retmode="text")
            seq_record = SeqIO.read(handle, "fasta")
            handle.close()
            sequences[species] = str(seq_record.seq)
        except Exception as e:
            print(f"Could not retrieve data for {species}: {e}")
    
    return sequences

# Function to insert genomic data into the database
def insert_genomic_data(sequences):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mereces",
        database="genome"
    )
    
    cursor = db.cursor()
    
    for species, sequence in sequences.items():
        # Insert into Genomic_data table (assuming species_id is fetched based on species name)
        cursor.execute(f"SELECT species_id FROM Species WHERE common_name = '{species.split(' ')[0]}'")
        species_id_result = cursor.fetchone()
        
        if species_id_result:
            species_id = species_id_result[0]
            insert_query = """
            INSERT INTO Genomic_data (species_id, source, sequence)
            VALUES (%s, %s, %s)
            """
            cursor.execute(insert_query, (species_id, species, sequence))
            db.commit()
            print(f"Data for {species} inserted successfully.")
        else:
            print(f"No species_id found for {species}")
    
    cursor.close()
    db.close()

# Function to compare genomic sequences and insert results into the comparison table
def compare_and_insert(sequences):
    aligner = PairwiseAligner()
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mereces",
        database="genome"
    )
    
    cursor = db.cursor()
    
    species_list = list(sequences.keys())
    for i in range(len(species_list)):
        for j in range(i + 1, len(species_list)):
            seq1 = sequences[species_list[i]]
            seq2 = sequences[species_list[j]]
            alignments = aligner.align(seq1, seq2)
            alignment = alignments[0]
            
            alignment_score = alignment.score
            mismatches = sum(1 for a, b in zip(alignment.target, alignment.query) if a != b and a != '-' and b != '-')
            
            # Insert comparison results into GENOME_COMPARISON table
            insert_query = """
            INSERT INTO GENOME_COMPARISON (species_id_1, species_id_2, alignment_score, mismatches)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(f"SELECT species_id FROM Species WHERE common_name = '{species_list[i].split(' ')[0]}'")
            species_id_1 = cursor.fetchone()[0]
            cursor.execute(f"SELECT species_id FROM Species WHERE common_name = '{species_list[j].split(' ')[0]}'")
            species_id_2 = cursor.fetchone()[0]
            
            cursor.execute(insert_query, (species_id_1, species_id_2, alignment_score, mismatches))
            db.commit()
            print(f"Comparison between {species_list[i]} and {species_list[j]} inserted successfully.")
    
    cursor.close()
    db.close()

# Main execution
sequences = fetch_sequences(accession_codes)
insert_genomic_data(sequences)
compare_and_insert(sequences)
