from Bio.Align import PairwiseAligner
import mysql.connector

# Database connection setup
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mereces",
    database="genome"
)

# Function to fetch all species and their sequences
def fetch_all_sequences():
    cursor = db.cursor()
    cursor.execute("SELECT Species_id, Sequence FROM Genomic_Data")
    results = cursor.fetchall()
    cursor.close()
    return results

# Function to insert comparison results into Genomic_Comparison table
def insert_comparison(species_id_1, species_id_2, alignment_score, mismatches):
    cursor = db.cursor()
    insert_query = """
        INSERT INTO Genome_Comparison (Species_id_1, Species_id_2, Alignment_score, Mismatches)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(insert_query, (species_id_1, species_id_2, alignment_score, mismatches))
    db.commit()
    cursor.close()

# Fetch all sequences
all_sequences = fetch_all_sequences()

# Initialize aligner
aligner = PairwiseAligner()

# Loop through each unique pair of sequences
for i in range(len(all_sequences)):
    species_id_1, seq1 = all_sequences[i]
    
    for j in range(i + 1, len(all_sequences)):  # Avoid duplicate pairs
        species_id_2, seq2 = all_sequences[j]
        
        # Perform alignment
        alignments = aligner.align(seq1, seq2)
        alignment = alignments[0]
        
        # Extract alignment score
        alignment_score = alignment.score
        
        # Count mismatches and gaps
        mismatches = sum(1 for a, b in zip(alignment.target, alignment.query) if a != b and a != '-' and b != '-')
        
        print(f"Alignment score for {species_id_1} vs {species_id_2}: {alignment_score}")


        # Insert into Genomic_Comparison table
        insert_comparison(species_id_1, species_id_2, alignment_score, mismatches)
        print(f"Inserted comparison for {species_id_1} vs {species_id_2}")

# Close the database connection
db.close()
print("All comparisons have been added to Genomic_Comparison.")
